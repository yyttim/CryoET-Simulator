# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 11:17
import mrcfile
import h5py
import numpy as np

# input_file_path = '../data/organelles/mitochondria/merged_file_perturbed.mrc'
# output_file_path = '../data/organelles/mitochondria/merged_file_perturbed.hdf'

# # 读取MRC文件
# with mrcfile.open(input_file_path) as mrc:
#     data = mrc.data
#
# # 将数据写入HDF文件
# with h5py.File(output_file_path, 'w') as hf:
#     hf.create_dataset('data', data=data, dtype='f4')


import mrcfile

# 打开.mrc文件
with mrcfile.open('../data/organelles/mitochondria/UE8-101-merged_file_perturbed2.mrc') as mrc:
    # 获取.mrc文件的尺寸
    dimensions = mrc.data.shape
    print("Dimensions of the protein file:", dimensions)