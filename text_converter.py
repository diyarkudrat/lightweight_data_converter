from .base_converter import BaseConverter

import csv

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