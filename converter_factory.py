from .ext_map import EXT_MAP

class ConverterFactory:
    @staticmethod
    def get_converter(file_extension):
        return EXT_MAP.get(file_extension)