# -*- coding: utf8 -*-

import cv2 as cv
import numpy as np
import math

img = np.zeros((200, 300, 3), np.uint8)
img[:][:] = (16, 41, 222)
h, w = img.shape[:2]

yellow = (0, 222, 255)
red = (16, 41, 222)

def get_point(center, r, angle):
    _y, _x = math.cos(angle) * r, math.sin(angle) * r
    return [center[0] -_x, center[1] - _y]

def drawStars(center, R, angle):

    global points
    points = []
    _r = R*math.sin(0.1*math.pi)/math.sin(0.7*math.pi)

    for i in range(5):
        points.append(get_point(center, R, angle))
        angle += 0.2*math.pi
        points.append(get_point(center, _r, angle))
        angle += 0.2*math.pi

    points=np.array([points], np.int32)
    cv.fillPoly(img, points, yellow, cv.LINE_AA)

drawStars((w*5/30,h*5/20), w/10, 0)
drawStars((w*10/30,h*2/20), w/30, math.atan(3/5) + math.pi/2)
drawStars((w*12/30,h*4/20), w/30, math.atan(1/7) + math.pi/2)
drawStars((w*12/30,h*7/20), w/30, math.atan(7/2))
drawStars((w*10/30,h*9/20), w/30, math.atan(5/4))

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()


