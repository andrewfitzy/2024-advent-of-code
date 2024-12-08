class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def is_in_bounds(
        self,
        start_x: int,
        start_y: int,
        width: int,
        height: int,
    ) -> bool:
        """
        tests if this point is within the given bounds of a rectangle
        """
        return self.x >= start_x and self.y >= start_y and self.x < start_x + width and self.y < start_y + height
