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
        text_content = []
        with open(input_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_content.append(page.extract_text())
        
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write("\n".join(text_content))

class ImageConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        img = Image.open(input_file_path)
        text = pytesseract.image_to_string(img)

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)

class TextConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        to_csv = kwargs.get("to_csv", False)

        if to_csv:
            with open(input_file_path, "r", encoding="utf-8") as input_file, \
                 open(output_path, "w", newline="", encoding="utf-8") as output_file:
                writer = csv.writer(output_file)

                for line in input_file:
                    writer.writerow([line.strip()])
        else:
            with open(input_file_path, "r", encoding="utf-8") as input_file, \
                 open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(input_file.read())

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
    parser = argparse.ArgumentParser(description="CLI for converting files to text or CSV.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("output_path", default=None, help="Path to the output file.")
    parser.add_argument("--to-csv", action="store_true", help="Convert the input file to CSV.")
    
    args = parser.parse_args()

    in_ext = os.path.splitext(args.input_file.lower())[1]
    output_path = args.output or ("output.csv" if args.to_csv else "output.txt")

    converter = ConverterFactory.get_converter(in_ext)
    if converter:
        converter.convert(args.input_file, output_path, to_csv=args.to_csv)
        print(f"Conversion complete. Output file: {output_path}")
    else:
        print("Unsupported file format.")

if __name__ == "__main__":
    main()