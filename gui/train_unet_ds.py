# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 9:03
import os
import shutil
import nrrd
import json
import time

import numpy as np
import pandas
from pprint import pprint
from polnet import lio

in_csv = '/root/autodl-tmp/polnet/gui/2024-10-30_14-54-02/tomos_motif_list.csv'
out_dir = '/root/autodl-tmp/data_unet/nnUNet_raw'

dataset_id = '003'
dataset_suffix = 'v01'

# fg_labels = {'membrane': (1, 2), 'ribo': tuple(range(3, 17))}
fg_labels = {'membrane': (1,), 'ribo': tuple(range(2, 3))}
fg_radii = {'membrane': 100, 'ribo': 32}
v_size_decimal = 1
VOI_OFFS = ((4, 496), (4, 496), (4, 196))

df = pandas.read_csv(in_csv, delimiter='\t')
tomos = set(df['Tomo3D'].tolist())
segs = dict()
for tomo in tomos:
    tomo_path, tomo_fname = os.path.split(tomo)
    segs[tomo] = tomo_path + '/tomo_lbls_' + tomo_fname.split('_')[2] + '.mrc'
assert len(tomos) == len(segs.keys())

# Create the dataset in nn-UNet format
out_dataset = out_dir + '/Dataset' + dataset_id + '_' + dataset_suffix
if os.path.exists(out_dataset):
    shutil.rmtree(out_dataset)
os.makedirs(out_dataset)
imgs_tr_dir, lbls_ts_dir = out_dataset + '/imagesTr', out_dataset + '/labelsTr'
print("imgs_tr_dir:", imgs_tr_dir)
print("lbls_ts_dir:", lbls_ts_dir)
os.mkdir(imgs_tr_dir)
os.mkdir(lbls_ts_dir)
out_labels = {'background': 0}

for tomo_id, tomo_in in enumerate(tomos):
    print('Processing tomogram:', tomo_in)
    tomo = lio.load_mrc(tomo_in)
    seg = lio.load_mrc(segs[tomo_in])
    seg_post = np.zeros(shape=seg.shape, dtype=np.uint8)
    for i, key in enumerate(fg_labels.keys()):
        print('\tProcessing label:', key)
        for lbl in fg_labels[key]:
            seg_post[seg == lbl] = i + 1
        out_labels[key] = i + 1
        out_labels[key] = i + 1
    nrrd.write(imgs_tr_dir + '/tomo_' + str(tomo_id).zfill(3) + '_0000.nrrd', tomo)
    nrrd.write(lbls_ts_dir + '/tomo_' + str(tomo_id).zfill(3) + '.nrrd', seg_post)

print("out_labels:")
pprint(out_labels)
# Json configuration file
dict_json = {
    'channel_names': {'0': 'rescale_to_0_1'},
    'labels': out_labels,
    'numTraining': len(tomos),
    'file_ending': '.nrrd'
}
with open(out_dataset + '/dataset.json', 'w') as outfile:
    outfile.write(json.dumps(dict_json, indent=4))

print('Successfully terminated. (' + time.strftime("%c") + ')')
