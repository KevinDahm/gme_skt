import cv2
import numpy as np



img_rgb = cv2.imread('find_chaos2.png')  # input screen shot of path of exile
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # turn it into gray



template_big = cv2.imread('chaos5_big.png',0) ## input big template
template_small = cv2.imread('chaos5_small.png',0) ## inpur small template

#small = cv2.resize(template,(45,45))

wb, hb = template_big.shape[::-1]
ws, hs = template_small.shape[::-1]

result_big = cv2.matchTemplate(img_gray, template_big, cv2.TM_CCOEFF_NORMED)
result_small = cv2.matchTemplate(img_gray, template_small, cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where(result_big >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0]+wb, pt[1]+hb), (0,255,255), 2)

loc = np.where(result_small >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0]+ws, pt[1]+hs), (0,255,255), 2)

##cv2.imshow('detected', img_rgb)

cv2.imwrite('detected.png', img_rgb)
##cv2.imwrite('chaos3.png', small)


##name = input("Type Something")

