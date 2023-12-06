import random
import turtle

from gui import RectangleGUI, PointGUI
from shapes import Point


# points are created with random coordinates
lower_left_point = Point(x=random.randint(0, 200), y=random.randint(0, 200))
upper_right_point = Point(x=random.randint(200, 400), y=random.randint(200, 400))

rectangle = RectangleGUI(lower_left_point, upper_right_point)

print("Rectangle coordinates: ")
rectangle.print_coordinates(is_lower_left=True)
rectangle.print_coordinates(is_lower_left=False)


# Get area and point from user
user_point = PointGUI(x=float(input("Guess x: ")), y=float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# print out the game result
print("Your point was inside rectangle: ", user_point.fall_inside_rect(rectangle))
print("Your area was off by: ", rectangle.calculate_area() - user_area)

my_turtle = turtle.Turtle()
rectangle.draw(canvas=my_turtle)
user_point.draw(my_turtle)

turtle.done()
