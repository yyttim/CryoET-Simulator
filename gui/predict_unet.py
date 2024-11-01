# -*- coding: utf-8 -*-

import os
import shutil
import nrrd
import time
import glob
import scipy as sp
import numpy as np

from polnet import lio

in_dir = "/root/autodl-tmp/TE_TEST"
out_dir = "/root/autodl-tmp/TE_TEST/nrrd/"
task_id = '001'
task_suffix = 'emp'
v_size_model = 12.44 # A/voxel
v_size_decimal = 1 # number of decimal to cut the voxel size precision
norm = True # If true intensity values are normalized wrt mean and variance

out_task = out_dir + '/Task' + task_id + '_' + task_suffix
if os.path.exists(out_task):
    shutil.rmtree(out_task)
os.makedirs(out_task)
imgs_ts_dir = out_task + '/imagesTs'
os.mkdir(imgs_ts_dir)

tomo_id = 1
for file_path in glob.iglob(in_dir + '/*.*'):
    if not (os.path.splitext(file_path)[1] in ['.mrc', '.rec']):
        continue
    print('Processing tomogram:', file_path)
    v_sizes = lio.read_mrc_v_size(file_path)
    v_sizes = (round(float(v_sizes[0]), v_size_decimal), round(float(v_sizes[1]), v_size_decimal),
               round(float(v_sizes[2]), v_size_decimal))
    if (v_sizes[0] != v_sizes[1]) or (v_sizes[0] != v_sizes[1]):
        print('\t-WARNING: this tomograms cannot pre processes due to its anisotropic voxel size ', v_sizes)
        continue
    v_size_tomo = v_sizes[0]
    tomo = lio.load_mrc(file_path).astype(np.float32)
    if norm:
        tomo.flags.writeable = True
        t_mean, t_std = tomo.mean(), tomo.std()
        tomo = (tomo - t_mean) / t_std
    if v_size_tomo != v_size_model:
        print('\t-Scaling input to tomogram from', v_size_tomo, 'A to fit the model voxel size of', v_size_model, 'A ...')
        tomo = sp.ndimage.zoom(tomo, v_size_tomo / v_size_model)
    nrrd.write(imgs_ts_dir + '/tomo_' + str(tomo_id).zfill(3) + '_0000.nrrd', tomo)
    tomo_id += 1

print('Successfully terminated. (' + time.strftime("%c") + ')')