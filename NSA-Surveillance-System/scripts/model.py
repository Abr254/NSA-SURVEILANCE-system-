from ultralytics import YOLO
import cv2

from config import MODEL_PATH

model = YOLO(MODEL_PATH)

def detect_plate():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model.predict(
            frame,
            conf=0.5
        )

        annotated = results[0].plot()

        cv2.imshow(
            "YOLO11 Plate Detection",
            annotated
        )

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()