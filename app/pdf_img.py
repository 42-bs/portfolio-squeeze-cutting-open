from PIL import Image
from typing import List
from pdf2image import convert_from_path


class PdfToImg:
    def __init__(self, pdf_path: str) -> None:
        self.pdf_path = pdf_path

    def pdf_to_img(self) -> List[Image.Image]:
        return convert_from_path(self.pdf_path)
