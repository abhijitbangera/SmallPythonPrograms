'''
	Author: Abhijit Bangera
	Python version: Python 3.x
	Description:
		Below code scans for images (.png,.jpg) in a given folder and then copies them
		to a new destination folder
	Pre-setup:
		Manually create a empty DestinationFolder in your destination path.
'''

import os
import shutil
src='C:\\Users\\xyz\\Desktop'
dst="C:\\Users\\xyz\\Desktop\\DestinationFolder"
files=os.listdir(src)
imageFormats=('.png','.jpg')
for file in files:
	if file.endswith(imageFormats):
		print (file) 
		shutil.copy(src+"\\"+str(file), dst)
