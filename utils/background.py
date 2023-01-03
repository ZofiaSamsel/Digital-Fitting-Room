import cv2


def load_background(button, bg_image):

	if button == ord("w"):
		bg_image = cv2.imread('images/backgrounds/2.png')
	elif button == ord("e"):
		bg_image = cv2.imread('images/backgrounds/1.png')
	elif button == ord("r"):
		bg_image = cv2.imread('images/backgrounds/3.png')
	elif button == ord("t"):
		bg_image = cv2.imread('images/backgrounds/4.png')
	elif button == ord("y"):
		bg_image = cv2.imread('images/backgrounds/5.png')
	elif button == ord("u"):
		bg_image = cv2.imread('images/backgrounds/7.png')
	elif button == ord("i"):
		bg_image = cv2.imread('images/backgrounds/1.webp')
	return bg_image