

# NSA-Surveillance System

## Vehicle Registration Plate Detection and Recognition using YOLO11 + PaddleOCR

## Overview

The **NSA-Surveillance System** is an Automatic Number Plate Recognition (ANPR) solution that combines **Ultralytics YOLO11** for license plate detection and **PaddleOCR** for optical character recognition (OCR). The system is designed for both research and real-time surveillance applications and can be deployed on embedded hardware or high-performance computing environments.

The project supports execution on **Google Colab**, **Kaggle Notebooks**, or a local machine with GPU acceleration. It can process images, videos, webcams, or RTSP/IP camera streams for continuous vehicle monitoring.

---

## Features

* 🚗 YOLO11-based vehicle license plate detection
* 🔍 PaddleOCR text recognition
* 📹 Supports webcam and RTSP/IP camera streams
* ☁️ Compatible with Google Colab and Kaggle
* 💻 GPU acceleration for faster inference
* 📊 Visualization using Matplotlib
* 📈 Detection confidence and OCR output logging
* 🔄 Easy integration with embedded hardware

---

# System Architecture

```
Camera
   │
   ▼
YOLO11 Detection
   │
   ▼
License Plate Cropping
   │
   ▼
PaddleOCR Recognition
   │
   ▼
Vehicle Registration Number
   │
   ▼
Display / Database / Alert System
```

---

# Hardware Requirements

## Development and Training Workstation

Recommended specifications:

| Component | Minimum            | Recommended                    |
| --------- | ------------------ | ------------------------------ |
| RAM       | 16 GB              | 32 GB                          |
| GPU       | 1 GB VRAM          | NVIDIA RTX Series (6 GB+ VRAM) |
| CPU       | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7             |
| Storage   | 20 GB Free         | SSD 100 GB+                    |

---

## Embedded Real-Time Deployment

### Raspberry Pi Model B

**Specifications**

* Broadcom BCM2835 SoC
* ARM1176JZF-S Processor
* 256 MB RAM
* 512 MB Storage (SD Card)
* GPIO interface
* Ethernet connectivity
* USB ports
* HDMI output

**Role**

* Model server
* Runs the trained detection pipeline
* Interfaces with cameras
* Sends processed information to the Arduino
* Displays results on the HMI

---

### Arduino Uno Rev3

**Microcontroller**

* ATmega328P (8-bit)

**Purpose**

* Human Machine Interface (HMI) controller
* Digital-to-analog signal conversion
* Controls external peripherals
* Receives processed data from Raspberry Pi through Serial communication

---

### HMI Display

**18-inch TFT LCD Monitor**

Purpose:

* Live surveillance display
* Bounding box visualization
* Display recognized registration numbers
* System monitoring dashboard

---

## Camera Support

The system supports:

* USB webcams
* CCTV cameras
* RTSP/IP cameras
* USB industrial cameras

---

# Software Stack

## Deep Learning

* Ultralytics YOLO11
* PaddleOCR
* TensorFlow

---

## Scientific Computing

* NumPy
* Pandas

---

## Visualization

* Matplotlib

---

## Development Environment

* Python 3.10+
* Google Colab
* Kaggle Notebooks
* Jupyter Notebook

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running YOLO Detection

```bash
python scripts/model.py
```

---

## Running PaddleOCR

```bash
python scripts/paddl_ocr.py
```

---

# Model Performance

## YOLO11

* Detection Model: YOLO11
* Training Epochs: 44
* Detection Accuracy: **77%**
* Limitation: Training stopped after reaching Google Colab compute limits.

### Future Improvements

Increasing the number of training epochs and expanding the dataset are expected to improve detection accuracy significantly.

---

## PaddleOCR

Current Results:

* OCR Accuracy: **88%**

Primary sources of OCR errors include:

* Blurred license plates
* Low-resolution images
* Dirty or noisy datasets
* Motion blur
* Poor lighting conditions

Expected production performance with cleaner datasets and optimized preprocessing:

* **98%+ recognition accuracy**

---

# Dataset

Training dataset downloaded using KaggleHub:

```python
import kagglehub

path = kagglehub.dataset_download(
    "sujaymann/car-number-plate-dataset-yolo-format"
)
```

Dataset:

**Car Number Plate Dataset (YOLO Format)**

Contains:

* Vehicle images
* YOLO annotation files
* Bounding boxes
* Multiple plate variations
* Ready-to-train dataset structure

---

# Python Modules

The project uses the following Python libraries:

```text
ultralytics
paddleocr
tensorflow
numpy
pandas
matplotlib
opencv-python
opencv-contrib-python
Pillow
kagglehub
scikit-learn
PyYAML
```

---

# Project Structure

```text
NSA-Surveillance-System/
│
├── datasets/
│
├── models/
│
├── scripts/
│   ├── model.py
│   ├── paddl_ocr.py
│   └── utils.py
│
├── outputs/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```