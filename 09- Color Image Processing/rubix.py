import numpy as np
import cv2

img = cv2.imread("rubix.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

#---yello

yello = np.uint8([[[0, 255, 255]]])
hsvyello = cv2.cvtColor(yello, cv2.COLOR_BGR2HSV)

lowerLimit = hsvyello[0][0][0] - 10, 100, 100
upperLimit = hsvyello[0][0][0] + 10, 255, 255

yello_L = np.array(lowerLimit)
yello_U = np.array(upperLimit)

yello_color = cv2.inRange(hsv, yello_L, yello_U)
yello_pix = np.where(yello_color != 0 )

img[yello_pix[0], yello_pix[1], 0] = 0
img[yello_pix[0], yello_pix[1], 1] = 0
img[yello_pix[0], yello_pix[1], 2] = 255

#----cyan

cyan = np.uint8([[[255, 255, 0]]])
hsvcyan = cv2.cvtColor(cyan, cv2.COLOR_BGR2HSV)

lowerLimit = hsvcyan[0][0][0] - 10, 100, 100
upperLimit = hsvcyan[0][0][0] + 10, 255, 255

cyan_L = np.array(lowerLimit)
cyan_U = np.array(upperLimit)

cyan_color = cv2.inRange(hsv, cyan_L, cyan_U)
cyan_pix = np.where(cyan_color != 0)

img[cyan_pix[0], cyan_pix[1], 0] = 255
img[cyan_pix[0], cyan_pix[1], 1] = 0
img[cyan_pix[0], cyan_pix[1], 2] = 0

#-----magenta

magenta = np.uint8([[[255, 0, 255]]])
hsvmagenta = cv2.cvtColor(magenta, cv2.COLOR_BGR2HSV)

lowerLimit = hsvmagenta[0][0][0] - 10, 100, 100
upperLimit = hsvmagenta[0][0][0] + 10, 255, 255

magenta_L = np.array(lowerLimit)
magenta_U = np.array(upperLimit)

magenta_color = cv2.inRange(hsv, magenta_L, magenta_U)

pixels = np.count_nonzero(magenta_color)
print(pixels)

magenta_pix = np.where(magenta_color != 0)

img[magenta_pix[0], magenta_pix[1], 0] = 0
img[magenta_pix[0], magenta_pix[1], 1] = 255
img[magenta_pix[0], magenta_pix[1], 2] = 0

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("rubix.jpg", img)
cv2.imshow("rubix", img)
cv2.waitKey()

