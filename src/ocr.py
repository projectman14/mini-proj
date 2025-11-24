# src/ocr.py
from PIL import Image
import cv2, pytesseract

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx=1.5, fy=1.5)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(Image.fromarray(img), lang='eng')
    return text.strip()
