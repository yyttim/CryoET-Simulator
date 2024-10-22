# -*- coding: utf-8 -*-
# @Time    : 2024/9/10 14:23

import mrcfile
import numpy as np
from scipy.ndimage import zoom

input_file_path  = '../data/organelles/mitochondria/UE8-101-merged_file_perturbed.mrc'
output_file_path = '../data/organelles/mitochondria/UE8-101-merged_file_perturbed_scale_10.mrc'

input_file_path  = '../data/organelles/mitochondria/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask.mrc'
output_file_path = '../data/organelles/mitochondria/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask_scale_10.mrc'

with mrcfile.open(input_file_path, mode='r') as mrc:
    # 获取原始数据
    original_data = mrc.data

    # 计算新的缩放比例
    zoom_factor = 0.4

    # 使用scipy的zoom函数进行下采样
    scaled_data = zoom(original_data, zoom_factor, order=3)

    with mrcfile.new(output_file_path, overwrite=True) as mrc_out:
        mrc_out.set_data(scaled_data.astype(np.float32))

        # 更新头信息的 cella 和 cellb
        mrc_out.header.cella['x'] /= 10
        mrc_out.header.cella['y'] /= 10
        mrc_out.header.cella['z'] /= 10

        # 更新原点坐标
        mrc_out.header.origin['x'] /= 10
        mrc_out.header.origin['y'] /= 10
        mrc_out.header.origin['z'] /= 10

        # 保存文件
        mrc_out.flush()