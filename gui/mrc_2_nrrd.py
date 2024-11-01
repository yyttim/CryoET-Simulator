# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 12:40
import SimpleITK as sitk

mrc_image = sitk.ReadImage('/root/autodl-tmp/EMPIAR-11370/Tomograms/TE2_tomo.rec.mrc')

sitk.WriteImage(mrc_image, '/root/autodl-tmp/EMPIAR-11370/Tomograms/nrrd/TE2_tomo.nrrd')
print("done.")