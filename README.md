# NSA-SURVEILANCE-system-
Pretrained ultralytics yolo v11 and paddle OCR for vehicle registration plates detection 
NSA system using YOLO + PaddleOCR

Features

- YOLO11 license plate detection
- PaddleOCR recognition
- Google Colab/kaggle 
- Ready for webcam or RTSP camera
Hardware for real time implementation 
-rasperry modelB BCM2835 256MBRAM, 512MBROM(model server)
-Arduino Ref3 with ATmega328P (8-bit)(for hmi digital to analogue from raspberry)
-HMI screen(18inch tft LCD display)
Compute resources and modules
-matplotlib(for visual assessment of model results)
-tensorflow
-numpy
-ultralytics installed 
-pandas
compute 
>16gb ram
>1gb graphics card 
```bash
pip install -r requirements.txt
```
```bash
python scripts/train.py
```
```bash
python scripts/predict.py
```
#description
YOLOv11 model=>accuracy 77% with 44 epochs which maxed out due to limited colab compute resources.
paddle OCR=> detection accuracy 88% with error rate highly contributed by unclean datasets, in contrast to realtime surveillance the model will surpass 98% accuracy.
#dataset
 kagglehub.dataset_download("sujaymann/car-number-plate-dataset-yolo-format")