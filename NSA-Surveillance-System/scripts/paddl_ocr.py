from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en'
)

image = "outputs/cropped_plates/plate.jpg"

result = ocr.ocr(image)

for line in result[0]:
    print(line[1][0])