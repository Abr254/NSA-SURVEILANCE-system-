
!pip install ultralytics 
!pip install ultralytics
!pip install paddleocr
!pip install paddlepaddle
!pip install opencv-python

from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
#yolo model initialization 