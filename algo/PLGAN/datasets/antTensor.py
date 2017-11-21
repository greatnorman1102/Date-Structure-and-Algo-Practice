# Copyright (c) 2017, Huawei Technologies.
# All rights reserved.
#
# antTensor
# Take HQ Antenna file (txt) and generate free space 3D tensor
# Tensor size: 224x224x224
# used as input data
#
# Usage: python antTensor.py 'path/to/the/file'
#
# Created by Xing Li, 09/27/2017
# Huawei Technologies, USA

import sys
import math
import numpy as np
import csv
from mayavi import mlab
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

def createTensor(antHeight, antFilePath, azumith=0, tilt=0, drawPat=False, savePat=False):
	# Create Antenna Tensor -------------------------------------------
	print('Reading Antenna File...')
	# Parse antenna variables from antenna file
	f = open(antFilePath)
	lines = f.readlines()

	# Parse general values and initialize variables for radiation pattern calculation
	# hz: [-180, 180], az: 2D pattern on azumith direction
	# vt: [-180, 180], el: 2D pattern on vertical direction
	name = antFilePath
	gain = float(lines[1])
	fmax = float(lines[3])
	fmin = float(lines[5])
	hz = []
	az = []
	vt = []
	el = []

	for l in lines[11:371]:
		elems = l.split("\t")
		if len(elems) == 2:
			elems = map(lambda x: x.strip(), elems)
		hz.append(float(elems[0])-180)
		az.append(float(elems[1]))
	for l in lines[372:-1]:
		elems = l.split("\t")
		if len(elems) == 2:
			elems = map(lambda x: x.strip(), elems)
		vt.append(float(elems[0])-180)
		el.append(float(elems[1]))

	print('Computing Antenna pattern %s...' % antFilePath)
	# Create 3D radiation pattern from 2D antenna pattern
	antPat = np.zeros((224, 224, 50))
	# Create 3D horizontal and vertical reference angle
	hzPat = np.zeros((224, 224, 50))
	vtPat = np.zeros((224, 224, 50))
	grid = 5
	c = 3*10**8 # speed of light 3x10^8 m/s
	feq = 2.1*10**6 # 2100 kHz, 2.1x10^6 Hz
	lamda = c/feq
	for x in range (224):
		for y in range (224):
			for z in range (50):
				# Convert tensor index to radian coordinate
				x_corrd, y_corrd, z_corrd = x-112, y-112, z-(50-antHeight)
				# Compute angle of azumith
				az_rad = math.atan2(y_corrd, x_corrd)
				az_deg = int(math.floor(az_rad*180/math.pi))
				hzPat[x,y,z] = az_deg # Filling the horizontal 
				# Compute angle of tilt
				az_len = math.sqrt(x_corrd**2+y_corrd**2)
				el_rad = math.atan2(z_corrd, az_len)
				el_deg = int(math.floor(el_rad*180/math.pi))
				vtPat[x,y,z] = el_deg
				# Calculate freespace loss at (az,el) angle
				if az_deg>=0:
					az_idx = az_deg-1
				else:
					az_idx = 359+az_deg
	
				if el_deg>=0:
					el_idx = el_deg-1
				else:
					el_idx = 359+el_deg
				L_ant = az[az_idx] - ((180-abs(az_deg))/180*(az[0]-el[el_idx])) + abs(az_deg)/180*(az[180-1]-el[180-el_idx])
				#print('Loss ant: %d' % L_ant)
				distance = grid * math.sqrt((x_corrd**2+y_corrd**2)+z_corrd**2)
				# Calculate distance loss
				FSPL = math.sqrt(math.pi*4*distance/lamda)
				#print('FSPL: %d' % FSPL)
				# Calculate PL at tensor location
				antPat[x,y,z] = round((gain - L_ant - FSPL),2)

	if drawPat:
		# Plot Antenna
		# Plot antenna 3D pattern surface (Require mayavi)
		#mlab.contour3d(hzPat)
		# Plot 2D radiation pattern at antenna height
		plt.imshow(antPat[:,:,0])
		plt.colorbar()
		plt.show()
	if savePat:
		# Save Antenna
		csv_f = open('./antenna_radPattern.csv', 'wb')
		writer = csv.writer(csv_f)
		writer.writerows(np.array(antPat).reshape(1, 224*224*50))
		csv_f.close()
	
	return antPat, hzPat, vtPat

antPat, hzPat, vtPat = createTensor(5, 'HBW-30.txt', drawPat=True)
