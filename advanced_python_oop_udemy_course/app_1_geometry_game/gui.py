from shapes import Point, Rectangle
import turtle


class RectangleGUI(Rectangle):

    def draw(self, canvas: turtle.Turtle) -> None:
        canvas.penup()
        canvas.goto(self.lower_left.x, self.lower_left.y)
        canvas.pendown()

        rect_width = self.upper_right.x - self.lower_left.x
        rect_height = self.upper_right.y - self.lower_left.y

        canvas.forward(distance=rect_width)
        canvas.left(angle=90)
        canvas.forward(distance=rect_height)
        canvas.left(angle=90)
        canvas.forward(distance=rect_width)
        canvas.left(angle=90)

        canvas.forward(distance=rect_height)


class PointGUI(Point):

    def draw(self, canvas: turtle.Turtle) -> None:
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()

        canvas.dot(size=10)