from .boat_race import (
    calculate_total_margin_for_error_for_all_records,
    calculate_margin_for_error_from_record
)


def test_part_one_example():
    result = calculate_total_margin_for_error_for_all_records("example.txt")

    assert result == 288


def test_part_two_example():
    result = calculate_margin_for_error_from_record("example.txt")

    assert result == 71503
