
import moviepy.editor as mp
from PIL import Image

def compressImg(storyId, myImage):

	img = Image.open(myImage)
	width, height = img.size 
	if width > 600 and height > 1200: 
		new_width  = 600
		new_height = 1200
		img = img.resize((new_width, new_height), Image.ANTIALIAS)
	img.save(storyId + '/Compressed.jpeg')
	
	
def compressVideo(storyId , myVideo):
	clip = mp.VideoFileClip(myVideo)
	height = clip.h
	if height > 480:
		clip_resized = clip.resize(height=360) 
	clip_resized.write_videofile(storyId + '/Compressed.mp4')


