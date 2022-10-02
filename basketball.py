#'''
import os, time
import pyscreenshot as ImageGrab
from Xlib import display
import cv2
import numpy as np
from pynput.mouse import Button, Controller

mouse = Controller()


def move_left():
	os.system("xte 'key Left'")

def move_right():
	os.system("xte 'key Right'")

def run():
	x = 50
	y = 150

	box = (x, y, x + 860, y + 700) 
	im = ImageGrab.grab(box)
	rgb_im = im.convert('RGB')

	rgb_im.save("im2.png")

	img_rgb = cv2.imread('im2.png')
	template = cv2.imread('im.png')
	w, h = template.shape[:-1]

	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = .8
	loc = np.where(res >= threshold)

	x = np.mean(loc[1]) + 50 + 32
	y = np.mean(loc[0]) + 150 + 55

	print(x,y)

	x_st = round((np.sqrt(739.0 * ((x-174.0)**2.0)*(y-115.0))-739.0*x+174.0*y-20010.0)/(y-854.0)) + 24
	print(x_st , 115 + 215)
#----------------------------------------
	template = cv2.imread('im3.png')
	w, h = template.shape[:-1]

	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = .8
	loc = np.where(res >= threshold)
	if loc[0].size > 0:
		slow = False
	else: 
		slow = True

	template = cv2.imread('im4.png')
	w, h = template.shape[:-1]

	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = .8
	loc = np.where(res >= threshold)
	if loc[0].size > 0:
		fast = False
	else: 
		fast = True
#----------------------------------------
	s = 0
	if not fast or not slow:
		r, g, b = rgb_im.getpixel((69, 190))
		s += (r + g + b) > 290;
		r, g, b = rgb_im.getpixel((90, 190))
		s += (r + g + b) > 290;
		r, g, b = rgb_im.getpixel((113, 190))
		s += (r + g + b) > 290;
		if not slow:
			x_st += 42 * s
		else:
			x_st -= 48 * s

	print(s)
	
	print(x_st , 115 + 215)
	mouse.position = (x_st, 330)

	mouse.click(Button.left, 1)
	time.sleep(1)
	mouse.click(Button.left, 1)
	time.sleep(1)


	return

def get_mouse():
	while True:	
		data = display.Display().screen().root.query_pointer()._data
		x = data["root_x"]
		y = data["root_y"]
		print (str(x), str(y))
		time.sleep(0.5)

def main():
	while True:
		run()
		time.sleep(9)


try:
	#get_mouse()
	'''
	x = 50
	y = 150

	box = (111, 329, 125, 352) 
	im = ImageGrab.grab(box)
	rgb_im = im.convert('RGB')

	rgb_im.save("im4.png")
	'''
	main()

except Exception as error:
	print (error)
