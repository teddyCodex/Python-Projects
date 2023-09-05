class Rectangle:
    def __init__(self, width, height) -> None:
        self.name = "Rectangle"
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        rows = self.height
        columns = self.width
        char = "*"
        output = str()
        if rows < 50 and columns < 50:
            for i in range(rows):
                output += f"{char * columns}\n"
            return output
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        area = self.get_area()
        area_shape = shape.get_area()
        return area // area_shape

    def __repr__(self) -> str:
        return f"{self.name}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, width) -> None:
        super().__init__(width, height=None)
        self.height = self.width

    def set_side(self, side):
        self.height, self.width = side, side

    def __repr__(self) -> str:
        return f"Square(side={self.width})"
