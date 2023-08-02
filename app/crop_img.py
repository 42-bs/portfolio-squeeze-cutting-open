from PIL import Image


class CropImg:
    def __init__(self, img: Image.Image, pos_to_crop: tuple) -> None:
        self.img = img
        self.pos_to_crop = pos_to_crop

    def crop(self) -> Image.Image:
        cropped_image = self.img.crop(self.pos_to_crop)
        return cropped_image
