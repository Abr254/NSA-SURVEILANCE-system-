import cv2

rtsp = "rtsp://username:password@ip:554/stream"

cap = cv2.VideoCapture(rtsp)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("RTSP Stream", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()