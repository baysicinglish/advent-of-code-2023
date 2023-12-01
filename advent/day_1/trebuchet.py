from enum import Enum
from num2words import num2words


class CalibrationValueNotFound(ValueError):
    pass


ONE_TO_TEN = Enum("Number", [num2words(num) for num in range(1, 10)])


def get_calibration_values(input_file, include_words=False):
    with open(f"day_1/inputs/{input_file}", "r") as file:
        calibration_values = [parse_calibration_value(line, include_words=include_words) for line in file]
    return tuple(calibration_values)


def parse_calibration_value(line, include_words=False):
    left_digit, right_digit = None, None
    left_pointer, right_pointer = 0, len(line) - 1

    while left_pointer <= right_pointer:
        if line[left_pointer].isdigit():
            left_digit = line[left_pointer]
            break
        elif include_words and (value := get_numerical_value(line[left_pointer:])):
            left_digit = value
            break
        left_pointer += 1

    while left_pointer <= right_pointer:
        if line[right_pointer].isdigit():
            right_digit = line[right_pointer]
            break
        elif include_words and (value := get_numerical_value(line[right_pointer:])):
            right_digit = value
            break
        right_pointer -= 1

    if not (left_digit and right_digit):
        raise CalibrationValueNotFound(f"Could not find a calibration value for line: {line}")

    return int(left_digit + right_digit)


def get_numerical_value(string):
    for value in ONE_TO_TEN:
        if string.startswith(value.name):
            return str(value.value)
    return None


if __name__ == "__main__":
    print(sum(get_calibration_values("challenge.txt")))
    print(sum(get_calibration_values("challenge.txt", include_words=True)))
