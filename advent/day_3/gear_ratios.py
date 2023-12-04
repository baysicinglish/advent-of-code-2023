from .matrices import Matrix, CoordinateOutOfBounds


def get_part_numbers(engine_schematic):
    with open(f"day_3/inputs/{engine_schematic}") as schematic:
        matrix = Matrix([line.strip() for line in schematic])

    current_part = ""
    is_valid_part = False

    for coordinate in matrix:
        if coordinate.value.isdigit():
            current_part += coordinate.value

            neighbours = coordinate.get_neighbours()
            if any(neighbour for neighbour in neighbours if not (neighbour.value.isdigit() or neighbour.value == ".")):
                is_valid_part = True

            if not is_end_of_row(coordinate):
                continue

        if is_valid_part and current_part:
            yield int(current_part)

        current_part = ""
        is_valid_part = False


def get_gears(engine_schematic):
    with open(f"day_3/inputs/{engine_schematic}") as schematic:
        matrix = Matrix([line.strip() for line in schematic])

    cogs = {}
    current_part = ""
    adjacent_cogs = set()

    for coordinate in matrix:
        if coordinate.value.isdigit():
            current_part += coordinate.value

            adjacent_cogs.update(
                (neighbour.x, neighbour.y)
                for neighbour in coordinate.get_neighbours() if neighbour.value == "*"
            )

            if not is_end_of_row(coordinate):
                continue

        if adjacent_cogs and current_part:
            for cog in adjacent_cogs:
                cogs[cog] = cogs.get(cog, []) + [int(current_part)]

        current_part = ""
        adjacent_cogs = set()

    return {cog: parts[0] * parts[1] for cog, parts in cogs.items() if len(parts) == 2}


def is_end_of_row(coordinate):
    try:
        coordinate.move(right=1)
        return False
    except CoordinateOutOfBounds:
        return True


if __name__ == "__main__":
    part_numbers = tuple(get_part_numbers("challenge.txt"))
    print(sum(part_numbers))

    gears = get_gears("challenge.txt")
    print(sum(gears.values()))
