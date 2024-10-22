# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 12:42
import mrcfile

def reset_tilt_angles(mrc_filename):
    with mrcfile.open(mrc_filename, mode='r+') as mrc:
        # 修改tilt angles信息
        mrc.header.tiltangles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        print("Tilt angles reset to zero.")

# 使用方法
reset_tilt_angles('test/recon.mrc')

# # 打开已有的MRC文件
# with mrcfile.open('test/tomo_rec_0_snr1.32.mrc', mode='r') as mrc:
#     # 读取数据
#     data = mrc.data
#
#     # 修改数据格式，例如，将数据转换为16位整数
#     new_data = data.astype(np.int16)
#
#     # 创建新的MRC文件并进行修改
#     with mrcfile.new('test/convert.mrc', overwrite=True) as new_mrc:
#         new_mrc.set_data(new_data)
#
#         # 修改header信息
#         new_mrc.header.map_mode = 1  # 16-bit integer
#         new_mrc.voxel_size = (12.44, 12.44, 12.44)  # 修改像素间距为12.44 Å
#
#         # 更新密度信息
#         new_mrc.header.dmin = new_data.min()
#         new_mrc.header.dmax = new_data.max()
#         new_mrc.header.dmean = new_data.mean()
#
#         # 如果需要，计算RMS deviation
#         new_mrc.header.rms = np.sqrt(np.mean((new_data - new_data.mean())**2))
#
#         # 修改倾斜角度
#         new_mrc.header.tiltangles = np.array([90.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float32)
#
#         print(f"New file created with updated header and data format.")