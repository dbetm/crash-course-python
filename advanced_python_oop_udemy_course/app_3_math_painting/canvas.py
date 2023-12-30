import numpy as np
from PIL import Image

from constants import ALLOWED_COLORS


class Canvas:

    def __init__(self, width: int, height: int, color: str):
        self.width = width
        self.height = height
        self.color = color

        assert color in ALLOWED_COLORS

        self.data = np.zeros((width, height, 3), dtype=np.uint8)
        self.data[:] = ALLOWED_COLORS[color]

    def make(self, imagepath: str) -> None:
        img = Image.fromarray(self.data, "RGB")

        img.save(fp=imagepath, format="png") 