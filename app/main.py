import os
from crop_img import CropImg
from pdf_img import PdfToImg


if __name__ == "__main__":
    file_path = "tech_draw.pdf"

    if not file_path:
        print("No file path entered. Exiting...")
    else:
        iPdfToImg = PdfToImg(file_path)
        images = iPdfToImg.pdf_to_img()

        iCropImgs = CropImg(images[0], (100, 400, 400, 900))
        cropped_image = iCropImgs.crop()

        cropped_image.save(os.path.join(os.getcwd(), "cropped_image.png"))
