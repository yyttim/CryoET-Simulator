# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 17:22
from core.vtk_utilities import *
from core.utilities import *
from core.widgets_utilities import *
from core.all_features2 import all_features2
from core.tk_utilities import *

DEF_PATH = os.path.realpath(os.getcwd() + '/../data') + '/../data_generated/polnet_test'

widget_out_dir = "/root/autodl-tmp/polnet/gui"

# MEMBRANES_LIST = ["F:/projectpython/polnet/data/in_mbs/ellipse.mbs"]
# HELIX_LIST = ["F:/projectpython/polnet/data/in_helix/actin.hns"]
MEMBRANES_LIST = []
HELIX_LIST = []
PROTEINS_LIST = ["/root/autodl-tmp/polnet/data/in_10A/1bxn_10A.pns"]
# 0：随机 1：高斯分布 2：梯度分布 3：对数正态分布 4：密度可调的均匀分布
PROTEINS_LIST_METHOD = [2, 0]
# 配合模式4 密度模式，指定个体数量
PROTEINS_LIST_DENSITY_LOOP = 20
# 是否开启单簇模式
PROTEINS_LIST_SINGLE_MODE = [True, False]
# 蛋白质开启扰动开关
PROTEINS_LIST_DISTRIBUTED = True
# PROTEINS_LIST = []
# MB_PROTEINS_LIST = ["/root/autodl-tmp/polnet/data/in_10A/mb_4pe5_10A.pms"]
MB_PROTEINS_LIST = []
ORGANELLE_LIST = ["/root/autodl-tmp/polnet/gui/merge_data_TE2/merged_10A.pns"]
# ORGANELLE_LIST = ["/root/autodl-tmp/polnet/data/xbq/2c4c_10.pns"]
# ORGANELLE_LIST = []
# 细胞器开启扰动开关
ORGANELLE_LIST_DISTRIBUTED = False

ntomos_widget = 1
voi_shape1 = 400
voi_shape2 = 400
voi_shape3 = 400
voi_off_widget_1 = 4
voi_off_widget_2 = 396
voi_off_widget_3 = 4
voi_off_widget_4 = 396
voi_off_widget_5 = 4
voi_off_widget_6 = 96
voi_size_widget = 10
mmer_tries_widget = 20
pmer_tries_widget = 100
surf_dec_widget = 0
malign_mn_widget = 1
malign_mx_widget = 1.5
malign_sg_widget = 0.2
detector_snr_widget_low = 1
detector_snr_widget_high = 2
widget_min = -60
widget_max = 61
widget_paso = 3


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
	if MEMBRANES_LIST or HELIX_LIST or PROTEINS_LIST or MB_PROTEINS_LIST or ORGANELLE_LIST:
		all_features2(ntomos_widget, generate_voi_shape(),
					  path, generate_voi_off(), voi_size_widget,
					  mmer_tries_widget, pmer_tries_widget,
					  MEMBRANES_LIST, HELIX_LIST, PROTEINS_LIST, MB_PROTEINS_LIST, ORGANELLE_LIST,
					  PROTEINS_LIST_METHOD, PROTEINS_LIST_DENSITY_LOOP, PROTEINS_LIST_SINGLE_MODE,
					  PROTEINS_LIST_DISTRIBUTED, ORGANELLE_LIST_DISTRIBUTED, surf_dec_widget,
					  generate_tilts_angs(), [detector_snr_widget_low, detector_snr_widget_high],
					  malign_mn_widget, malign_mx_widget, malign_sg_widget)
