# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 15:03
import mrcfile
import numpy as np
from scipy.ndimage import zoom

input_file_path  = '../data/organelles/mitochondria/UE8-101-mitochondrial_inner_membrane-1.0_segmentationmask.mrc'
output_file_path = '../data/organelles/mitochondria/UE8-101-merged_file_perturbed_scale_10.mrc'

input_file_path  = '../data/organelles/mitochondria/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask.mrc'
output_file_path = '../data/organelles/mitochondria/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask_scale_10.mrc'

input_file_path  = '../data/organelles/ER/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask.mrc'
output_file_path = '../data/organelles/ER/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask_scale_10.mrc'

input_file_path  = '../data/organelles/ER/UE8-102-endoplasmic_reticulum_membrane-1.0_segmentationmask.mrc'
output_file_path = '../data/organelles/ER/UE8-102-endoplasmic_reticulum_membrane-1.0_segmentationmask_scale_10.mrc'

# # 打开 MRC 文件
# with mrcfile.open(input_file_path, permissive=True) as mrc:
#     data = mrc.data.copy()  # 复制数据以便后续操作
#
# # 计算缩放因子
# scale_factor = 0.5
#
# # 使用 zoom 函数缩小数据
# scaled_data = zoom(data, (scale_factor, scale_factor, scale_factor), order=1)
#
# # 计算新的像素间距
# new_pixel_spacing = [ps / scale_factor for ps in (12.44, 12.44, 12.44)]
#
# # 创建新的 MRC 文件保存缩小后的数据
# with mrcfile.new(output_file_path, overwrite=True) as new_mrc:
#     new_mrc.set_data(scaled_data.astype(np.uint8))
#     new_mrc.voxel_size = new_pixel_spacing
#
# print("模型已缩小并保存至 'scaled_model.mrc'")

with mrcfile.open(input_file_path, mode='r+') as mrc:
    data = mrc.data

    resized_data = zoom(data, 0.5)

    with mrcfile.new(output_file_path, overwrite=True) as output_mrc:
        output_mrc.set_data(resized_data.astype(np.float32))

print("缩小后的模型已保存至 'output.mrc'")