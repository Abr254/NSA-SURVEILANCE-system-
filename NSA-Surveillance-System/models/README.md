# Models

This directory stores trained and pretrained YOLO11 models.

## Example

```
models/
├── best.pt
├── last.pt
└── README.md
```

## Model Description

### best.pt

Best-performing YOLO11 weights after training.

### last.pt

Checkpoint from the final training epoch.

## Training Summary

| Model | Epochs | Detection Accuracy |
|--------|--------|-------------------|
| YOLO11 | 44 | 77% |

Training stopped after 44 epochs due to Google Colab compute limitations.

## Future Improvements

- Train for 100–300 epochs
- Increase dataset size
- Tune learning rate
- Use larger YOLO11 variants