from .scratchcards import calculate_scratchcard_points


class TestGetScratchcardPoints:
    def test_returns_points(self):
        points = tuple(calculate_scratchcard_points("example.txt"))

        assert points == (8, 2, 2, 1, 0, 0)
