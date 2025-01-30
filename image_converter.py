from .base_converter import BaseConverter

import pytesseract
from PIL import Image

class ImageConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        img = Image.open(input_file_path)
        text = pytesseract.image_to_string(img)

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)