import cv2
import os

def save_crop(image, box, filename):
    x1, y1, x2, y2 = map(int, box)
    crop = image[y1:y2, x1:x2]

    os.makedirs("outputs/cropped_plates", exist_ok=True)

    cv2.imwrite(
        f"outputs/cropped_plates/{filename}",
        crop
    )

    return crop