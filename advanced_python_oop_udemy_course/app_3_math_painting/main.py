from __future__ import annotations
from typing import List

from canvas import Canvas
from constants import ALLOWED_COLORS
from shapes import Rectangle, Square, Shape


canvas_color = "white"
canvas = Canvas(400, 400, canvas_color)

shapes_ : List[Shape] = list()

print(f"Canvas is height: {canvas.height} and width: {canvas.width}")

allowed_colors_for_shapes = ALLOWED_COLORS.copy()
allowed_colors_for_shapes.pop(canvas_color)
allowed_colors_for_shapes = list(allowed_colors_for_shapes.keys())


while True:
    opt = input("\nChoose a shape to draw: rectangle or square: ").lower()

    x = int(input("Type x coordinate: "))
    y = int(input("Type y coordinate: "))

    if opt == "rectangle":
        width = int(input("Type width: "))
        height = int(input("Type height: "))
        color = input(f"Choose a color {allowed_colors_for_shapes}: ")

        rect = Rectangle(x, y, width, height, color)
        shapes_.append(rect)

    elif opt == "square":
        side = int(input("Type side lenght: "))
        color = input(f"Choose a color {allowed_colors_for_shapes}: ")

        square = Square(x, y, side, color)
        shapes_.append(square)
    else:
        print("No allowed shape")

    more_flag = input("Type q to quit, or anything else to continue: ")

    if more_flag == "q":
        break


for shape_ in shapes_:
    shape_.draw(canvas)

canvas.make("example.png")