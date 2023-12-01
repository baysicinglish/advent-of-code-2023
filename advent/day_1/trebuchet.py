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
    left_pointer, right_pointer = 0, len(line) - 1

    def get_closest_number(pointer):
        nonlocal left_pointer

        while left_pointer <= pointer <= right_pointer:
            if line[pointer].isdigit():
                return line[pointer]
            elif include_words and (value := get_numerical_value(line[pointer:])):
                return value

            if pointer == left_pointer:
                left_pointer = pointer = pointer + 1
            else:
                pointer -= 1

    left_digit = get_closest_number(left_pointer)
    right_digit = get_closest_number(right_pointer)

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
