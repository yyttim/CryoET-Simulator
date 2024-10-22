# -*- coding: utf-8 -*-
# @Time    : 2024/9/26 17:22

import os
import datetime
from core.vtk_utilities import *
from core.utilities import *
from core.widgets_utilities import *
from core.all_features2 import all_features2
from core.tk_utilities import *

DEF_PATH = os.path.realpath(os.getcwd() + '/../data') + '/../data_generated/polnet_test'

widget_out_dir = "/root/autodl-tmp/simulation"

MEMBRANES_LIST = []
HELIX_LIST = []
PROTEINS_LIST = [
	"/root/autodl-tmp/polnet/data/proteins/pns/4ug0.pns",
]
# 蛋白质开启扰动开关
PROTEINS_LIST_DISTRIBUTED = [0]
# 是否开启单簇模式
PROTEINS_LIST_SINGLE_MODE = [1]
# 0：随机 1：高斯分布 2：梯度分布 3：对数正态分布 4：密度可调的均匀分布, 5:指定范围数量
PROTEINS_LIST_METHOD      = [4]
# 配合模式4 密度模式，指定个体数量
PROTEINS_LIST_DENSITY_LOOP = [1]
# 配合模式5 指定个体数量
PROTEINS_LIST_POS_LOOP = [1]
MB_PROTEINS_LIST = []
ORGANELLE_LIST = [
	# "/root/autodl-tmp/polnet/data/organelles/mitochondria/UE8-101-merged_file_perturbed.pns",
	# "/root/autodl-tmp/polnet/data/organelles/mitochondria/TE2-102-endoplasmic_reticulum_membrane-1.0_segmentationmask.pns",
	# "/root/autodl-tmp/polnet/data/organelles/mitochondria/UE3-100-merged_file_perturbed.pns",
	# "/root/autodl-tmp/polnet/gui/merge_data_TE2/merged_10A.pns",
]
# 细胞器开启扰动开关
ORGANELLE_LIST_DISTRIBUTED = False

ntomos_widget = 10
voi_shape1 = 64
voi_shape2 = 64
voi_shape3 = 64
voi_off_widget_1 = 0
voi_off_widget_2 = voi_shape1 - voi_off_widget_1
voi_off_widget_3 = 0
voi_off_widget_4 = voi_shape2 - voi_off_widget_3
voi_off_widget_5 = 0
voi_off_widget_6 = voi_shape3 - voi_off_widget_5
voi_size_widget = 1
mmer_tries_widget = 1
pmer_tries_widget = 100
surf_dec_widget = 0.5
malign_mn_widget = 0
malign_mx_widget = 0
malign_sg_widget = 0
detector_snr_widget_low = 100
detector_snr_widget_high = 100
widget_min = -60
widget_max = 61
widget_paso = 2


def generate_voi_shape():
	return (voi_shape1, voi_shape2, voi_shape3)


def generate_tilts_angs():
	return range(widget_min, widget_max, widget_paso)


def generate_voi_off():
	return ((voi_off_widget_1, voi_off_widget_2),
			(voi_off_widget_3, voi_off_widget_4),
			(voi_off_widget_5, voi_off_widget_6))


if __name__ == "__main__":
	path = check_dir(widget_out_dir, DEF_PATH)

	timestamp = datetime.datetime.now().timestamp()
	dt_object = datetime.datetime.fromtimestamp(timestamp)
	folder_name = dt_object.strftime("%Y-%m-%d_%H-%M-%S")
	path = os.path.join(path, folder_name)
	os.makedirs(folder_name)
	if MEMBRANES_LIST or HELIX_LIST or PROTEINS_LIST or MB_PROTEINS_LIST or ORGANELLE_LIST:
		all_features2(ntomos_widget, generate_voi_shape(),
					  path, generate_voi_off(), voi_size_widget,
					  mmer_tries_widget, pmer_tries_widget,
					  MEMBRANES_LIST, HELIX_LIST, PROTEINS_LIST, MB_PROTEINS_LIST, ORGANELLE_LIST,
					  PROTEINS_LIST_METHOD, PROTEINS_LIST_DENSITY_LOOP, PROTEINS_LIST_POS_LOOP, PROTEINS_LIST_SINGLE_MODE,
					  PROTEINS_LIST_DISTRIBUTED, ORGANELLE_LIST_DISTRIBUTED, surf_dec_widget,
					  generate_tilts_angs(), [detector_snr_widget_low, detector_snr_widget_high],
					  malign_mn_widget, malign_mx_widget, malign_sg_widget)
