# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 11:20
import h5py
import matplotlib.pyplot as plt

output_file_path = '../data/organelles/mitochondria/merged_file_perturbed.hdf'
# 读取HDF文件中的数据
with h5py.File(output_file_path, 'r') as hf:
    data = hf['data'][:]

# 显示折中处理后的二维图像
print(data.shape, data.shape[0] // 2)
plt.imshow(data[data.shape[0] // 2+50, :, :], cmap='viridis')
plt.colorbar()
plt.show()


# import h5py
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
#
# output_file_path = '../data/organelles/mitochondria/merged_file_perturbed.hdf'
#
# # 读取HDF文件中的数据
# with h5py.File(output_file_path, 'r') as hf:
#     data = hf['data'][:]
#
# # 创建三维图形
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 生成网格
# x, y, z = np.meshgrid(np.arange(data.shape[2]), np.arange(data.shape[1]), np.arange(data.shape[0]))
#
# # 将数据绘制为三维图形
# ax.scatter(x, y, z, c=data.flatten(), cmap='viridis')
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# plt.show()