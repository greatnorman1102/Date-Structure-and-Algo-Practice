# !/usr/bin/env python
# !encoding:utf-8

import os
from load_map import MapReader
import time
from opts import *
import csv
import numpy as np

count = 0
width_pix = 224
height_pix = 224
x_step_m = 120
y_step_m = 120
patch_per_iter = 500
map_path = args.path

dirs = os.listdir(map_path)
dirs.sort()
print(dirs)

for dir in dirs:
	map_current = MapReader(map_path=os.path.join(map_path, dir),
                            w_pix=width_pix,
                            h_pix=height_pix,
                            x_step_m=x_step_m,
                            y_step_m=y_step_m,
                            patch_lim_per_iter=patch_per_iter)
	total_patch_no_temp = int(map_current.total_patch_no)
	patch_row_idx, patch_col_idx = 0, 0
	start_time = time.time()
	print("total number of patches for %s = {}".format(total_patch_no_temp) % dir)


    #open(os.path.join(map_current.map_path, 'dump.csv'), 'w').close()


    # print map_current.building.mat
	while total_patch_no_temp > 0:
		data, idx, site_locations, bs_params, patch_row_idx_temp, patch_col_idx_temp = \
            map_current.GenPatchInLoop(patch_row_idx, patch_col_idx, count)

		patch_row_idx = patch_row_idx_temp
		patch_col_idx = patch_col_idx_temp

		total_patch_no_temp = int(map_current.total_patch_no \
                              - (patch_col_idx * map_current.total_patch_no_row + patch_row_idx))

		print("total patch left = {}".format(total_patch_no_temp))	
        # not all patches can generate valid data
		count = count + idx
		print("count = {}".format(count))

	#print(np.array(data).shape)
	#print("===")
	
	#if idx > 0:
	    #print(np.array(data).reshape(idx, 3, 50176))
	    # print(np.array(data).reshape(idx, 150528))
	 #   with open(os.path.join(map_current.map_path, 'dump.csv'), 'a+b') as csv_f:
         #       writer = csv.writer(csv_f)
         #       writer.writerows(np.array(data).reshape(idx, 150528))
	#print("---")

	print("{} map patches generated for the city of '{}' in {} seconds".format(count, dir, time.time()-start_time))
	count = 0
    
	print(map_current.map_path)
	print(map_current.building)
	print(map_current.clutter)
	print(map_current.dem)
	print(map_current.width_pix)
	print(map_current.height_pix)
	print(map_current.x_step_m)
	print(map_current.y_step_m)
	print(map_current.patch_lim_per_iter)
	print(map_current.x_step_pix)
	print(map_current.y_step_pix)
	print(map_current.total_patch_no_row)
	print(map_current.total_patch_no_col)
	print(map_current.total_patch_no)
