"""
Pexpect makes Python a better tool for controlling other applications.\
Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output.
"""
import pexpect
import os
from config import *
from PIL import Image

current_dir = os.getcwd()
command = DARKNET_BINARY_LOCATION + " detector test " + DARKNET_DATA_FILE + " " + DARKNET_CFG_FILE \
			+ " " + DARKNET_WEIGHTS + " -ext_output -dont_show"

image_path = os.path.join(current_dir, 'complex.jpg')
"""
To run the code on the production side \
It is important to automate the terminal command \
./darknet detector test custom/text.data custom/cfg/text.cfg backup/text_2000.weights 3341407.jpeg -ext_output -dont_show -out
To accomplish this task proc is used
"""
proc = pexpect.spawn(command)
proc.expect('Enter Image Path:')
proc.sendline(image_path)
proc.expect('Enter Image Path:', timeout=90)
result = proc.before
decode_result = result.decode('utf-8')
split_result = decode_result.split('\n')
"""
When we get the area where the text is detected \
It is cropped
"""
def crop_image(image, area):
	img_read = Image.open(image)
	img_crop = img_read.crop(area)
	return img_crop 
"""
This code is used to get the area \
as well as saving the cropped images
"""
count = 0
for i in split_result:
	if 'left_x' in i:
		data = i.split()
		x = int(data[3])
		y = int(data[5])
		w = int(data[7])
		h = int(data[9][:-1])
		area = (x,y,(x+w),(y+h))
		cropped_image = crop_image(image_path, area)
		cropped_image.save("predictions{}.png".format(count))
		count+=1
