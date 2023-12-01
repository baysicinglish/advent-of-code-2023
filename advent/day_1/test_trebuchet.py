from .trebuchet import get_calibration_values


class TestGetCalibrationValues:
    def test_gets_calibration_values_for_example(self):
        values = get_calibration_values("part_one_example.txt")

        assert values == (12, 38, 15, 77)
