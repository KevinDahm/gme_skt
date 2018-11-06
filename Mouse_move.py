import pyautogui
import time
#import cv2
#import numpy as np

from Image_Search import Temp_Match as TM 
#from Image_Search.Temp_Match import chaos_finder as cf;
#i = 100
#while i<1000:

#	pyautogui.moveTo(i,i,duration=0.05)
#	i = i +50

#print(TM.chaos_finder())


def hover_coords(coord_list):
	for point in coord_list:
		x = point[0]
		y = point[1]
		pyautogui.moveTo(point[0]+5,point[1]+5,duration=0.05)
		#pyautogui.click()
		time.sleep(0.5)


time.sleep(5)
hover_coords(TM.chaos_finder()) 

#print(TM.chaos_finder())