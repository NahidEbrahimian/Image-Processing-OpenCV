import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)

height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))

video_writer = cv2.VideoWriter('color_detection.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width, height), 0)

while True:

    rec, frame = video_cap.read()
    if not rec:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    width, height = gray_frame.shape
    roi = gray_frame[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100]

    color_average = np.average(roi)
    if color_average < 80 :
        color = "Black"
        font_color = (0, 0, 0)

    elif color_average < 160:
        color = "Gray"
        font_color = (60, 60, 60)

    else:
        color = "White"
        font_color = (150, 150, 150)

    frame_blur = cv2.blur(gray_frame, (60, 60))
    frame_blur[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100] = roi

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