from .matrices import Matrix, Coordinate


class TestCoordinate:
    def test_get_neighbouring_coordinates(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        coordinate = Coordinate(1, 1, matrix)
        neighbours = coordinate.get_neighbours()
        neighbour_values = tuple(neighbour.value for neighbour in neighbours)

        assert neighbour_values == (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_get_neighbouring_coordinates_in_corner(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        coordinate = Coordinate(2, 2, matrix)
        neighbours = coordinate.get_neighbours()
        neighbour_values = tuple(neighbour.value for neighbour in neighbours)

        assert neighbour_values == (5, 6, 8, 9)

    def test_value_logic(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        coordinate = Coordinate(2, 0, matrix)

        assert coordinate.value == 3
