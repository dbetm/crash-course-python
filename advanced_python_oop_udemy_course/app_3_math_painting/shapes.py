from abc import ABC, abstractmethod 

from canvas import Canvas
from constants import ALLOWED_COLORS


class Shape(ABC):

    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

        assert color in ALLOWED_COLORS

    @abstractmethod
    def draw(self, canvas: Canvas) -> None:
        pass


class Square(Shape):

    def __init__(self, x: int, y: int, side: int, color: str):
        self.side = side
        super().__init__(x, y, color)
    
    def draw(self, canvas: Canvas):
        rgb = ALLOWED_COLORS[self.color]

        canvas.data[self.y:self.y+self.side, self.x:self.x+self.side] = rgb



class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        self.width = width
        self.height = height
        super().__init__(x, y, color)
    
    def draw(self, canvas: Canvas):
        rgb = ALLOWED_COLORS[self.color]

        canvas.data[self.y:self.y+self.height, self.x:self.x+self.width] = rgb