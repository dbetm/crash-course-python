class Rectangle:

    def __init__(self, lower_left, upper_right):
        """Receive the points."""
        self.lower_left: Point = lower_left
        self.upper_right: Point = upper_right
    
    def calculate_area(self) -> float:
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y

        return width * height

    def print_coordinates(self, is_lower_left: bool) -> None:
        if is_lower_left:
            print(f"({self.lower_left.x}, {self.lower_left.y})")
        else:
            print(f"({self.upper_right.x}, {self.upper_right.y})")


class Point:

    # it could be 'self' or another thing, but the convention is to use self
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    

    def fall_inside_rect(self, rectangle: Rectangle) -> bool:
        is_inside_x_axis = (
            self.x >= rectangle.lower_left.x and self.x <= rectangle.upper_right.x
        )

        is_inside_y_axis = (
            self.y >= rectangle.lower_left.y and self.y <= rectangle.upper_right.y
        )

        return is_inside_x_axis and is_inside_y_axis
