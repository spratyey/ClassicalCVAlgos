
import cv2
import numpy as np

input1 = cv2.imread(
	"/home/praty/Documents/coursework/3-2/CV/assignment-1-spratyey/images/Section-1/calib-object.jpg", cv2.IMREAD_COLOR)


def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, ' ', y)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', input1)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
