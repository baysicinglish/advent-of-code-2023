
def get_calibration_values(input_file):
    with open(f"day_1/inputs/{input_file}", "r") as file:
        calibration_values = [parse_calibration_value(line) for line in file]
    return tuple(calibration_values)


def parse_calibration_value(line):
    left_pointer, right_pointer = 0, len(line) - 1

    while not line[left_pointer].isdigit():
        left_pointer += 1
    left_digit = line[left_pointer]

    while not line[right_pointer].isdigit():
        right_pointer -= 1
    right_digit = line[right_pointer]

    return int(left_digit + right_digit)


if __name__ == "__main__":
    print(sum(get_calibration_values("part_one.txt")))
