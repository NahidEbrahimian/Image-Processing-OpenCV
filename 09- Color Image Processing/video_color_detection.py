import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)

height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))

video_writer = cv2.VideoWriter('video_color_detection.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width, height))

def ROI_RGB2HSV(color, hsv_roi):

    hsvcolor = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    if color[0][0][0] == 66:
        lowerLimit = hsvcolor[0][0][0] - 0, 10, 10
        upperLimit = hsvcolor[0][0][0] + 10, 100, 100
    elif color[0][0][0] == 0 and color[0][0][1] == 0 and color[0][0][2] == 0:
        lowerLimit = hsvcolor[0][0][0] - 0, 0, 0
        upperLimit = hsvcolor[0][0][0] + 10, 10, 10

    elif color[0][0][0] == 0 and color[0][0][1] == 0 and color[0][0][2] == 255:
        lowerLimit = hsvcolor[0][0][0] - 0, 100, 100
        upperLimit = hsvcolor[0][0][0] + 10, 255, 255

    else:
        lowerLimit = hsvcolor[0][0][0] - 10, 100, 100
        upperLimit = hsvcolor[0][0][0] + 10, 255, 255

    color_L = np.array(lowerLimit)
    color_U = np.array(upperLimit)
    roi_hsv_color = cv2.inRange(hsv_roi, color_L, color_U)

    return roi_hsv_color

while True:

    rec, frame = video_cap.read()
    if not rec:
        break

    width, height, _ = frame.shape
    roi = frame[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100, :]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    color = "None"
    font_color = (255, 255, 255)
    max_pixels = 0

    # -----blue
    rgb_color = np.uint8([[[255, 0, 0]]])
    roi_blue_color =  ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_blue_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "blue"
        font_color = (255, 0, 0)

    # -----green
    rgb_color = np.uint8([[[0, 255, 0]]])
    roi_green_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_green_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "green"
        font_color = (0, 255, 0)

    # -----red
    rgb_color = np.uint8([[[0, 0, 255]]])
    roi_red_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_red_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "red"
        font_color = (0, 0, 255)

    # ---yello
    rgb_color = np.uint8([[[0, 255, 255]]])
    roi_yello_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_yello_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "yello"
        font_color = (0, 255, 255)

    # ----cyan
    rgb_color = np.uint8([[[255, 255, 0]]])
    roi_cyan_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_cyan_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "cyan"
        font_color = (255, 255, 0)

    # -----magenta
    rgb_color = np.uint8([[[255, 0, 255]]])
    roi_magenta_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_magenta_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "magenta"
        font_color = (255, 0, 255)

    # -----gray
    rgb_color = np.uint8([[[66, 66, 66]]])
    roi_gray_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_gray_color[:, :])
    if pixels > max_pixels:
        max_pixels = pixels
        color = "gray"
        font_color = (66, 66, 66)

    # -----black
    rgb_color = np.uint8([[[0, 0, 0]]])
    roi_black_color = ROI_RGB2HSV(rgb_color, hsv_roi)
    pixels = np.count_nonzero(roi_black_color)
    if pixels > max_pixels:
        max_pixels = pixels
        color = "black"
        font_color = (0, 0, 0)


    frame_blur = cv2.blur(frame, (60, 60))
    frame_blur[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100, :] = roi

    cv2.putText(frame_blur, color, (width // 12, height // 12), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color, 1,
                    cv2.LINE_AA)

    cv2.imshow('color', frame_blur)
    video_writer.write(frame_blur)

    if cv2.waitKey(10) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('Result.jpg', frame_blur)
        break

video_cap.release()
video_writer.release()