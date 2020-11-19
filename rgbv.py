#detecting RGB objects

import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)


green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )

blue = np.uint8([[[255,0,0 ]]])
hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
print( hsv_blue )

red = np.uint8([[[0,0,255 ]]])
hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
print( hsv_red )


lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

lower_green = np.array([50,50,50])
upper_green = np.array([255,60,255])

lower_red = np.array([10,50,50])
upper_red = np.array([255,255,10])


while(1):

    _, frame = video.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask1 = cv.inRange(frame, lower_blue, upper_blue)
    mask2 = cv.inRange(frame, lower_green, upper_green)
    mask3 = cv.inRange(frame, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask= mask1 | mask2 | mask3)

    cv.imshow("Mask_Blue",mask1)
    cv.imshow("Mask_Green",mask2)
    cv.imshow("Mask_Red",mask3)
    cv.imshow("Frame",frame)
    cv.imshow("Final",res)
    
    key = cv.waitKey(1) & 0xFF

    if key == 27:
        break



video.release()

cv.destroyAllWindows()