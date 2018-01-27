import os
import cv2
import numpy as np
import pandas as pd


imagefolder =  ""
csvfolder = ""
finalimages = ""
finalcsvs = ""

for file in os.listdir(imagefolder):
	image = cv2.imread(imagefolder+"\\"+file)
	print("its working")
	shape = image.shape
	shape =list(shape)
	

                    #add image dimensions to the if else block according to your need
                    #modify the resize ratios according to your desired outputsize
	#this script resizes to 96*96 by default
	if shape[0] == 720:
		image = cv2.resize(image,(0,0), fx=1/6.4, fy=1/3.6)
		cv2.imwrite(finalimages+"\\"+ file,image)		
		
	else:
		image = cv2.resize(image,(0,0), fx=1/9.6, fy=1/5.4)
		cv2.imwrite(finalimages+"\\"+ file,image)
	
	
			

