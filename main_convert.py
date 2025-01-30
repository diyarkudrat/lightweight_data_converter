from .converter_factory import ConverterFactory

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="CLI for converting files to text or CSV.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("--output", default=None, help="Path to the output file.")
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