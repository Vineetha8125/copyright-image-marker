# src/ocr_extractor.py

import pytesseract
from PIL import Image
import os

def extract_ocr_text(image_dir):
    ocr_results = []

    for file in os.listdir(image_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            image_path = os.path.join(image_dir, file)
            try:
                text = pytesseract.image_to_string(Image.open(image_path))
                ocr_results.append({
                    'image_file': file,
                    'ocr_text': text.lower().strip()
                })
            except Exception as e:
                print(f"OCR failed for {file}: {e}")
    
    return ocr_results
