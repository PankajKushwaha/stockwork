import os
import moviepy.video.io.ImageSequenceClip
image_folder='/home/pankaj/Pictures/reel/'
symbol=os.listdir("/home/pankaj/Pictures/reel")[0].split("_")[1].split(".")[0]
fps=1

image_files = [os.path.join(image_folder,img)
               for img in os.listdir(image_folder)
               if img.endswith(".png")]

#print(sorted(image_files))
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted(image_files), fps=fps)
filename=image_folder+symbol+'_reel.mp4'
clip.write_videofile(filename)
copyFileCommand="cp "+filename+" /home/pankaj/Pictures/reeldb/"
os.system(copyFileCommand)

