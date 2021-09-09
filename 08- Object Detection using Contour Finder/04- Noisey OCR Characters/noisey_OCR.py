import numpy as np
import cv2


img_gray = cv2.imread("Inputs/noisey_OCR.jpg", cv2.IMREAD_GRAYSCALE)

img_gray = cv2.medianBlur(img_gray, 3)
img_gray = cv2.medianBlur(img_gray, 3)
ret,thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
dilated = cv2.dilate(thresh, kernel, iterations = 10)


# ------------extract lines-----------
lines = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
lines = lines[0] if len(lines) == 2 else lines[1]

# --------------for each line-------------
n = 1
for cnt in lines:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)

    if area > 200:
        Xb = []
        Yb = []
        Wb = []
        Hb = []

        img = img_gray[y + 5 : y + h - 5, x + 5 : x + w - 5]
        img_thresh = thresh[y + 5 : y + h - 5, x + 5 : x + w - 5]

        # ---------------extract all characters in line----------------
        characters = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        characters = characters[0] if len(characters) == 2 else characters[1]

        # ---------------for each character append x, y, w, h----------------
        for char in characters:
            area = cv2.contourArea(char)
            x, y, w, h = cv2.boundingRect(char)

            if area > 20:
                Xb.append(x)
                Yb.append(y)
                Wb.append(w)
                Hb.append(h)

        Xb = np.stack(Xb, axis=0)
        Yb = np.stack(Yb, axis=0)
        Wb = np.stack(Wb, axis=0)
        Hb = np.stack(Hb, axis=0)

        # ---------------each character compared with other characters in line----------------
        for i in range(0, len(Xb)):
            flag = 1

            for j in range(i, len(Xb)):

                if i == len(Xb) - 1 and flag == 1:
                    character = img[Yb[i]: Yb[i] + Hb[i], Xb[i]: Xb[i] + Wb[i]]
                    cv2.imwrite(f"Output/noisey_OCR_characters/char{n}.jpg", character)
                    cv2.rectangle(img, (Xb[i], Yb[i]), (Xb[i] + Wb[i], Yb[i] + Hb[i]), (100, 100, 100), 2)
                    n = n+1
                    flag = 0

                elif j > i and Xb[i] != -1 and Xb[j] != -1 and flag == 1:

                    if ((np.absolute(Yb[j] - Yb[i]) < 10) and (np.absolute(Xb[j] - Xb[i]) < 5) and flag == 1) or ((np.absolute(Yb[j] + Hb[j] - Yb[i]) < 10) and (np.absolute(Xb[j] - Xb[i]) < 5) and flag == 1):
                        x1 = np.minimum(Xb[j], Xb[i])
                        y1 = np.minimum(Yb[j], Yb[i])
                        x2 = np.maximum(Xb[j] + Wb[j], Xb[i] + Wb[i])
                        y2 = np.maximum(Yb[j] + Hb[j], Yb[i] + Hb[i])
                        w = np.absolute(x1 - x2)
                        h = np.absolute(y1 - y2)
                        character = img[y1 : y1 + h, x1 : x1 + w]
                        cv2.imwrite(f"Output/noisey_OCR_characters/char{n}.jpg", character)
                        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 0), 2)
                        n = n+1
                        flag = 0
                        Xb[i] = -1
                        Xb[j] = -1

                    elif (np.absolute(Xb[j] - Xb[i]) < 11) and (np.absolute(Yb[j] - Yb[i]) < 5) and flag == 1:
                        x1 = np.minimum(Xb[j], Xb[i])
                        y1 = np.minimum(Yb[j], Yb[i])
                        x2 = np.maximum(Xb[j] + Wb[j], Xb[i] + Wb[i])
                        y2 = np.maximum(Yb[j] + Hb[j], Yb[i] + Hb[i])
                        w = np.absolute(x1 - x2)
                        h = np.absolute(y1 - y2)
                        character = img[y1 : y1 + h, x1 : x1 + w]
                        cv2.imwrite(f"Output/noisey_OCR_characters/char{n}.jpg", character)
                        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 0), 2)
                        n = n+1
                        flag = 0
                        Xb[i] = -1
                        Xb[j] = -1

            if Xb[i] != -1 and flag == 1:
                character = img[Yb[i]: Yb[i] + Hb[i], Xb[i]: Xb[i] + Wb[i]]
                cv2.imwrite(f"Output/noisey_OCR_characters/char{n}.jpg", character)
                cv2.rectangle(img, (Xb[i], Yb[i]), (Xb[i] + Wb[i], Yb[i] + Hb[i]), (100, 100, 100), 2)
                n = n+1
                flag = 0


cv2.imwrite(f"Output/noisey_OCR_characters/noisey_OCR.jpg", img_gray)
cv2.imshow("image_gray", img_gray)
cv2.waitKey()


