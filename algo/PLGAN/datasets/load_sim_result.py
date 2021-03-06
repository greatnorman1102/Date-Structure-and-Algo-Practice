# !/usr/bin/env python
# !encoding:utf-8

import numpy as np
import scipy.ndimage
import os
import scipy.misc

def FetchSimResult(map_path, w, h):
	with open(os.path.join(map_path, 'result.csv'), 'r') as csv_f:
		data = np.loadtxt(csv_f, delimiter=',', skiprows=0)

    # # first column is the indices, unsorted.
    # idx = data[{{}, {1}}]:int():squeeze()
    # return idx, data[{{}, {2, data:size()[2]}}]:float():view(-1, 10, 10)
	idx = data[:,0].astype(np.int)
	mat_temp = data[:,1:].astype(np.float)
	mat = mat_temp.reshape((mat_temp.shape[0], w, h))
	# Save path
	save_path = os.path.join(map_path, 'GT')
	if not os.path.exists(save_path):
    		os.makedirs(save_path)
	# generate visualize patch Add by Xing Li
	sim3Ch = np.zeros((224,224,3))
	for i in range (len(mat)):
		temp_sim_56 = mat[i]
		temp_sim_224 = scipy.ndimage.zoom(temp_sim_56, 4, order=0)
		# Normalize matrix to image range
		#temp_sim_224 *= 255.0/temp_sim_224.max()
		# Flip the sim result upside down to match the map coordinate
		sim3Ch[:,:,0] = sim3Ch[:,:,1] = sim3Ch[:,:,2] = np.flipud(temp_sim_224)
		scipy.misc.imsave((save_path + '/sim_%d.jpg' % idx[i]), sim3Ch)

	return 0
#    return idx, mat

if __name__=='__main__':
	PLwidth = 56
	PLheight = 56
	map_path = '/home/xing/maps-20m/'
	dirs = os.listdir(map_path)
	dirs.sort()
	print(dirs)

	for dir in dirs:
		if dir == ('Beijing' or 'Changsha' or 'Dongguan'):
			print(dir)
			continue
		else:
			print('Working on: %s' % dir)
			sim_path = os.path.join(map_path, dir)
			FetchSimResult(map_path=sim_path+'/simulation-results/', w=PLwidth, h=PLheight)
			print('Done.')
