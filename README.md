# Lightweight Data Converter for LLM Windows

## Description

A minimal, extensible command-line tool for converting files (PDF, text, images) to either plain text or CSV format. Useful for preparing content for language models or similar applications.

## Features

- **PDF to Text** using PyPDF2  
- **Image to Text** using pytesseract (OCR)  
- **Text to CSV** using Python's built-in `csv` module  
- **Easily Extensible** via a factory design pattern

## Installation

1. **Clone or Download** this repository.  
2. **Install Dependencies**:
   ```bash
   pip install PyPDF2 pytesseract pillow