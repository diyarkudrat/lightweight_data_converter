import argparse
import csv
import os
import PyPDF2
import pytesseract

from PIL import Image

class BaseConverter:
    def convert(self, input_file_path, output_path, **kwargs):
        raise NotImplementedError("Subclasses must implement convert()")

class PDFConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        raise NotImplemented

class ImageConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        raise NotImplemented

class TextConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        raise NotImplemented

class ConverterFactory:
    @staticmethod
    def get_converter(file_extension, **kwargs):
        ext_map = {
            ".pdf": PDFConverter(),
            ".png": ImageConverter(),
            ".jpg": ImageConverter(),
            ".jpeg": ImageConverter(),
            ".txt": TextConverter(),
        }

        return ext_map.get(file_extension, None)

def main():
    raise NotImplemented