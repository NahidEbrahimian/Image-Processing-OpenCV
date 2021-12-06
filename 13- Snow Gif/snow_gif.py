import cv2
import numpy as np
import imageio


def img_read():

    img = cv2.imread("snow3.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (500, 500))
    return img

img = img_read()
width, height, _ = img.shape

snow_list = []
num_snow = 1000
for i in range(num_snow):
    y_position = np.random.randint(0, height)
    x_position = np.random.randint(0, width)
    snow_speed = np.random.randint(3, 7)
    snow_size = np.random.randint(1, 3)
    change_x = np.random.randint(-2, 2)

    snow_list.append([y_position, x_position, snow_speed, snow_size, change_x])


snow_img = []
for j in range(50):

    img = img_read()

    for i in range(num_snow):
        if snow_list[i][0] > 490:
            snow_list[i][0] = 0

        snow_size = snow_list[i][3]
        snow_speed = snow_list[i][2]
        change_x = snow_list[i][4]

        img[snow_list[i][0]: snow_list[i][0]+snow_size, snow_list[i][1]: snow_list[i][1]+snow_size, :] = 255

        snow_list[i][0] = snow_list[i][0] + snow_speed
        snow_list[i][1] = snow_list[i][1] + change_x

    snow_img.append(img)

with imageio.get_writer(("snow.gif"), mode="I") as writer:
    for idx, img in enumerate(snow_img):
        writer.append_data(img)