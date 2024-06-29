# import cv2 library 
import cv2 
import numpy as np

def vconcat_resize(img_list, interpolation 
				= cv2.INTER_CUBIC): 
	w_min = min(img.shape[1] 
				for img in img_list) 
	
	im_list_resize = [cv2.resize(img, 
					(w_min, int(img.shape[0] * w_min / img.shape[1])), 
								interpolation = interpolation) 
					for img in img_list] 
	return cv2.vconcat(im_list_resize) 

# read the images 
img1 = cv2.imread('TCS.png') 
img2 = cv2.imread('NTPC.png')
img3 = cv2.imread('VEDL.png')

im_v = vconcat_resize([img1,img2,img3])

# show the output image
cv2.imwrite('result.png', im_v)

