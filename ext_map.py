from .pdf_converter import PDFConverter
from .image_converter import ImageConverter
from .text_converter import TextConverter

EXT_MAP = {
    ".pdf": PDFConverter(),
    ".png": ImageConverter(),
    ".jpg": ImageConverter(),
    ".jpeg": ImageConverter(),
    ".tiff": ImageConverter(),
    ".txt": TextConverter(),
}
