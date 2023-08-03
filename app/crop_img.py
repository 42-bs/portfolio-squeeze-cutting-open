from PIL import Image
from typing import List, Tuple


class CropImg:
    def __init__(
        self,
        img: Image.Image or List[Image.Image],
        box: Tuple[int, int, int, int],
    ) -> None:
        self.img = img
        self.box = box
        self.new_img: Image.Image or List[Image.Image] = None

    def crop(self) -> Image.Image or List[Image.Image]:
        if isinstance(self.img, list):
            self.new_img = [img.crop(self.box) for img in self.img]
            return self.new_img
        else:
            self.new_img = self.img.crop(self.box)
            return self.new_img
