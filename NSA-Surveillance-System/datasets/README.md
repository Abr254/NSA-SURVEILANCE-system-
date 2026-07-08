# Dataset

This project uses a YOLO-format vehicle registration plate dataset obtained from KaggleHub.

## Download

```python
import kagglehub

path = kagglehub.dataset_download(
    "sujaymann/car-number-plate-dataset-yolo-format"
)
```

After downloading, extract the dataset into the `datasets/` directory.

Expected structure:

```
datasets/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── data.yaml
```

## Dataset Format

- Images (.jpg/.png)
- YOLO annotation files (.txt)
- Bounding boxes for license plates

## Notes

- Ensure `data.yaml` points to the correct dataset paths.
- Additional data augmentation is recommended to improve model robustness.
- Higher quality datasets generally improve OCR accuracy. NJ