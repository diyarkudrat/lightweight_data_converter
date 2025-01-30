from .base_converter import BaseConverter

import PyPDF2

class PDFConverter(BaseConverter):
    def convert(self, input_file_path, output_path, **kwargs):
        text_content = []
        with open(input_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_content.append(page.extract_text())
        
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write("\n".join(text_content))