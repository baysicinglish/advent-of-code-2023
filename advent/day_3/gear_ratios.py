

def get_part_numbers(engine_schematic):
    with open(f"day_3/inputs/{engine_schematic}") as schematic:
        lines = [line.strip() for line in schematic]

    for line_number, line in enumerate(lines):
        current_part = ""
        valid_part = False

        for char_position, char in enumerate(line):
            if char.isdigit():
                current_part += char

                # is important part
                for check_line in [lines[line_number + offset] for offset in range(-1, 2) if 0 <= line_number + offset <= len(lines) - 1]:
                    for check_char in [check_line[char_position + offset] for offset in range(-1, 2) if 0 <= char_position + offset <= len(line) - 1]:
                        if not (check_char.isdigit() or check_char == "."):
                            valid_part = True
            else:
                if valid_part and current_part:
                    yield int(current_part)

                current_part = ""
                valid_part = False

        if valid_part and current_part:
            yield int(current_part)


def get_gears(engine_schematic):
    gears = {}

    with open(f"day_3/inputs/{engine_schematic}") as schematic:
        lines = [line.strip() for line in schematic]

    for line_number, line in enumerate(lines):
        current_part = ""
        adjacent_gears = []

        for char_position, char in enumerate(line):
            if char.isdigit():
                current_part += char

                for check_line_num in [line_number + offset for offset in range(-1, 2) if 0 <= line_number + offset <= len(lines) - 1]:
                    for check_char_num in [char_position + offset for offset in range(-1, 2) if 0 <= char_position + offset <= len(line) - 1]:
                        if lines[check_line_num][check_char_num] == "*":
                            gear_name = f"x{check_char_num}y{check_line_num}"
                            if gear_name not in adjacent_gears:
                                adjacent_gears.append(gear_name)

            else:
                if adjacent_gears and current_part:
                    for gear in adjacent_gears:
                        gears[gear] = gears.get(gear, []) + [int(current_part)]

                current_part = ""
                adjacent_gears = []

        if adjacent_gears and current_part:
            for gear in adjacent_gears:
                gears[gear] = gears.get(gear, []) + [int(current_part)]

    return {gear: parts[0] * parts[1] for gear, parts in gears.items() if len(parts) == 2}


if __name__ == "__main__":
    part_numbers = tuple(get_part_numbers("challenge.txt"))
    print(sum(part_numbers))

    gears = get_gears("challenge.txt")
    print(sum(gears.values()))
