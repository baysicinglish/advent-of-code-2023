from typing import Sequence, Any


class CoordinateOutOfBounds(Exception):
    pass


class Matrix:
    def __init__(self, array: Sequence[Sequence[Any]]):
        self.array = array

    def __iter__(self):
        for row_number, row in enumerate(self.array):
            for column_number in range(len(row)):
                yield self.get_coordinate(column_number, row_number)

    def get_coordinate(self, x, y):
        if not (0 <= y < len(self.array) and 0 <= x < len(self.array[y])):
            raise CoordinateOutOfBounds(f"Coordinate[{x}, {y}] is outside of Matrix")
        return Coordinate(x, y, self)


class Coordinate:
    def __init__(self, x, y, matrix: Matrix):
        self.matrix = matrix
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinate[{self.x}, {self.y}]"

    @property
    def value(self):
        return self.matrix.array[self.y][self.x]

    def get_neighbours(self):
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                try:
                    yield self.matrix.get_coordinate(self.x + x_offset, self.y + y_offset)
                except CoordinateOutOfBounds:
                    pass

    def move(self, *, up=0, down=0, left=0, right=0):
        vertical_offset = up - down
        horizontal_offset = right - left
        return self.matrix.get_coordinate(self.x + horizontal_offset, self.y + vertical_offset)
