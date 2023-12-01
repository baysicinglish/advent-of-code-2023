import pytest

from .trebuchet import (
    get_calibration_values,
    get_numerical_value,
    parse_calibration_value,
    CalibrationValueNotFound
)


class TestGetCalibrationValues:
    def test_gets_calibration_values_for_part_one(self):
        values = get_calibration_values("part_one_example.txt")

        assert values == (12, 38, 15, 77)

    def test_gets_calibration_values_for_part_two(self):
        values = get_calibration_values("part_two_example.txt", include_words=True)

        assert values == (29, 83, 13, 24, 42, 14, 76)


class TestParseCalibrationValue:
    def test_raises_exception_if_no_value_in_input(self):
        line = "therearenonumbersinhere"

        with pytest.raises(CalibrationValueNotFound):
            parse_calibration_value(line)


class TestGetNumericalValue:
    def test_get_numerical_value(self):
        line = "two1nine"

        value = get_numerical_value(line)

        assert value == "2"
