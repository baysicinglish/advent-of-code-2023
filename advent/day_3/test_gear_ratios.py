from .gear_ratios import get_part_numbers


class TestGetPartNumbers:
    def test_returns_part_numbers_for_example_schematic(self):
        example_schematic = "example.txt"

        part_numbers = get_part_numbers(example_schematic)

        part_numbers = tuple(part_numbers)
        assert part_numbers == (467, 35, 633, 617, 592, 755, 664, 598)
        assert sum(part_numbers) == 4361
