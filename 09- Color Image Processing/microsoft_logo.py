import numpy as np
import cv2


def get_optimal_font_scale(text, width):

    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=scale/10, thickness=1)
        new_width = textSize[0][0]
        if (new_width <= width):
            return scale/10
    return 1


sahpe_0 = int(input("Enter Height:"))
sahpe_1 = sahpe_0 * 2
img = np.ones((sahpe_0, sahpe_1, 3), dtype = np.uint8)

# img = np.ones((300, 600, 3), dtype = np.uint8)
img = img * 60

b_h = img.shape[0]//3
b_w = img.shape[1]//6

img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w : b_w + ((b_w * 2) // 4) - 2, 0] = 0
img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w : b_w + ((b_w * 2) // 4) - 2, 1] = 50
img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w : b_w + ((b_w * 2) // 4) - 2, 2] = 255

img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 0] = 0
img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 1] = 200
img[b_h : b_h + ((b_h * 2) // 4) - 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 2] = 180

img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 0] = 0
img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 1] = 150
img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w + ((b_w * 2) // 4) + 2 : b_w * 2, 2] = 255

img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w : b_w + ((b_w * 2) // 4) - 2, 0] = 255
img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w : b_w + ((b_w * 2) // 4) - 2, 1] = 150
img[b_h + ((b_h * 2) // 4) + 2 : b_h * 2, b_w : b_w + ((b_w * 2) // 4) - 2, 2] = 0

font_size = get_optimal_font_scale('Microsoft', 3 *b_w)
cv2.putText(img, 'Microsoft', (((2*b_h ) + (b_h // 4)), (1*b_w + (3*(b_w // 4)))), cv2.FONT_ITALIC, font_size, (255, 255, 255), 5,
            cv2.LINE_AA)

# FONT_HERSHEY_SIMPLEX
# FONT_ITALIC
cv2.imwrite("Microsoft.jpg", img)
cv2.imshow("img", img)
cv2.waitKey()


