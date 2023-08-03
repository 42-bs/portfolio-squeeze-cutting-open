import os
import sys

from crop_img import CropImg
from pdf_img import PdfToImg


if __name__ == "__main__":
    file_path = "pdf/tech_draw.pdf"

    if not file_path:
        print("No file path entered. Exiting...")
    else:
        iPdfToImg = PdfToImg(file_path)
        images = iPdfToImg.pdf_to_img()
        
        iCropImgs = CropImg(images, (100, 0, 1000, 2000))
        iCropImgs.crop()
        for img in iCropImgs.new_img:
            img.show()
