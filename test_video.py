import cv2
import numpy as np
import os
import time

image_folder = '/home/pankaj/Pictures/reel'
video_name = '/home/pankaj/Pictures/video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

video = cv2.VideoWriter(video_name, fourcc, 1, (width,height))
count = 0
for image in images:
    count = count+1
    print(count)
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

