import os, time
import pyscreenshot as ImageGrab
from Xlib import display


def move_left():
	os.system("xte 'key Left'")

def move_right():
	os.system("xte 'key Right'")

def exist_branch(x, y):
	box = (x, y - 4 * 100, x+1, y) 
	im = ImageGrab.grab(box)
	rgb_im = im.convert('RGB')

	x, y = im.size

	result = []
	for i in range(0, 5):
		
		r, g, b = rgb_im.getpixel((0, y - i*99 - 1))
		summa = r + g + b;
		print(y - i*99 - 1, summa)
		if summa < 700:
			result.append(True)
		else:
			result.append(False)

	return result

def get_mouse():
	while True:	
		data = display.Display().screen().root.query_pointer()._data
		x = data["root_x"]
		y = data["root_y"]
		print (str(x), str(y), exist_branch(x, y))

def main():
	start_x = 567
	start_y = 576

	while True:
		branches = exist_branch(start_x, start_y)
		
		cons_str = ""
		for elem in branches:
			if elem:
				cons_str += 'Left  '
			else:
				cons_str += 'Right '
		print (cons_str)

		for elem in branches:
			if elem:
				move_left()
				time.sleep(0.03)
				move_left()

			else:
				move_right()
				time.sleep(0.03)
				move_right()
		time.sleep(0.03)

try:
	#get_mouse()
	time.sleep(5)
	main()
except Exception as error:
	print (error)	