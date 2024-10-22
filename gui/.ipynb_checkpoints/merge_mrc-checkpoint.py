# -*- coding: utf-8 -*-
# @Time    : 2024/9/21 10:45
import os
import mrcfile

mrc_file_a = "merge_data_TE2/100-mitochondrial_outer_membrane-1.0_segmentationmask.mrc"
mrc_file_b = "merge_data_TE2/101-mitochondrial_inner_membrane-1.0_segmentationmask.mrc"

with mrcfile.open(mrc_file_a) as mrc1:
    data1 = mrc1.data
    voxel_size1 = mrc1.voxel_size
    dimensions1 = mrc1.data.shape

with mrcfile.open(mrc_file_b) as mrc2:
    data2 = mrc2.data
    voxel_size2 = mrc2.voxel_size
    dimensions2 = mrc2.data.shape

if voxel_size1 != voxel_size2 or dimensions1 != dimensions2:
    raise ValueError("The voxel sizes or dimensions of the input files are not the same.")

merged_data = (data1 + data2)

output_filename = os.path.join(os.path.dirname(mrc_file_a), 'merged_file.mrc')
with mrcfile.new(output_filename, overwrite=True) as mrc:
    mrc.set_data(merged_data)
    mrc.voxel_size = voxel_size1
