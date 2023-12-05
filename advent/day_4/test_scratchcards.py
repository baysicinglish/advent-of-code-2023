from .scratchcards import calculate_scratchcard_points, calculate_total_scratchcards


class TestCalculateScratchcardPoints:
    def test_returns_points(self):
        points = tuple(calculate_scratchcard_points("example.txt"))

        assert points == (8, 2, 2, 1, 0, 0)


class TestCalculateTotalScratchcards:
    def test_returns_total_count(self):
        count = calculate_total_scratchcards("example.txt")

        assert count == 30
