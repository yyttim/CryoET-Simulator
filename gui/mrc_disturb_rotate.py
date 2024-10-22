# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 21:07
import mrcfile
import numpy as np
from scipy.ndimage import rotate

input_file_path  = '../data/proteins/mrc/4ug0.mrc'
output_file_path = '../data/proteins/mrc/4ug0_disturb.mrc'

with mrcfile.open(input_file_path, mode='r') as mrc:
    original_data = mrc.data
    header = mrc.header

    mask = original_data > 0.1

    perturbed_data = original_data.copy()
    perturbed_data[mask] += np.random.normal(scale=0.5, size=perturbed_data[mask].shape).astype(np.float32)

    # Rotate
    random_angle = np.random.uniform(0, 360)
    rotated_data = rotate(perturbed_data, angle=random_angle, axes=(1, 2), reshape=False, mode='nearest')

    with mrcfile.new(output_file_path, overwrite=True) as new_mrc:
        new_mrc.set_data(rotated_data)
        for key in header.dtype.names:
            new_mrc.header[key] = header[key]