from pdb import set_trace as st
import os
from PIL import Image
from skimage import img_as_float
from skimage.measure import compare_mse as mse
from skimage.measure import compare_psnr as psnr
import numpy as np
import cv2
import glob
import math

def get_sorted_files(Directory):
	filenamelist = []
	for root, dirs, files in os.walk(Directory):
		for name in files:
			fullname = os.path.join(root, name)
			filenamelist.append(fullname)
	return sorted(filenamelist)

def rmse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return math.sqrt(err)

def rmsdiff(im1, im2):
    """Calculates the root mean square error (RSME) between two images"""
    return math.sqrt(mse(im1, im2))

img_Output = []
img_GT = []
diff = []

print("Reading Folder Output")
filenames_Output = get_sorted_files('/home/xing/pix2pix/results/map2simAnt/latest_net_G_train/images/output/')
filenames_Output.sort(key=lambda f: int(filter(str.isdigit, f)))
for img in filenames_Output:
	temp = cv2.imread(img)
	temp_resize = cv2.resize(temp, (56, 56))
	img_Output.append(temp_resize)

print("Reading Folder GT")
filenames_GT = get_sorted_files('/home/xing/pix2pix/results/map2simAnt/latest_net_G_train/images/target/')
filenames_GT.sort(key=lambda f: int(filter(str.isdigit, f)))
for img in filenames_GT:
	temp = cv2.imread(img)
	temp_resize = cv2.resize(temp, (56, 56))
	img_GT.append(temp_resize)

for i in range (len(img_Output)):
	diff.append(rmsdiff(img_Output[i], img_GT[i]))
	#diff.append(rmse(img_Output[i], img_GT[i]))
	
#print(img_GT[0][:,:,1]/255.0)
#print(diff)
print('Mean RMSE: %d, Max Error: %d, Min Error: %d' % (np.mean(diff), np.max(diff), np.min(diff)))
