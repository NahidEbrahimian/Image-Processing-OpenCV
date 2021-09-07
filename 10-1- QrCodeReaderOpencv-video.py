import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)
height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_writer = cv2.VideoWriter('QrCode-Reader-opencv1.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (width, height))

def QrCode_Reader(frame):
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if bbox is not None:

        n_lines = len(bbox)
        for i in range(n_lines):
            coordinates = np.asarray(bbox[i], dtype='int')

            cv2.rectangle(frame, (coordinates[0][0], coordinates[0][1]), (coordinates[2][0], coordinates[2][1]),
                          color=(255, 255, 0), thickness=3)

    return frame, data

while True:

    rec, frame = video_cap.read()
    if not rec:
        break

    width, height, _ = frame.shape
    roi = frame[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100, :]
    frame, data = QrCode_Reader(frame)

    frame_blur = cv2.blur(frame, (60, 60))
    frame_blur[width // 2 - 100 : width // 2 + 100, height // 2 - 100 : height // 2 + 100, :] = roi

    cv2.putText(frame_blur, data, (width // 6, height // 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1,
                    cv2.LINE_AA)

    cv2.imshow('QrCode-Reader', frame_blur)
    video_writer.write(frame_blur)

    if cv2.waitKey(10) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('QrCode-Reader.jpg', frame_blur)
        break

video_cap.release()
video_writer.release()