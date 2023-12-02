from typing import Tuple


def get_possible_games(results_log, available_cubes):
    with open(f"day_2/inputs/{results_log}") as results:
        for line in results:
            game_number, min_cubes_needed = parse_line(line)
            if not is_cube_count_exceeded(available_cubes, min_cubes_needed):
                yield game_number


def parse_line(line: str) -> Tuple[int, dict[str, int]]:
    """
    Returns the game number and the maximum count per colour of cube revealed during the game.
    Expects game information in the form `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`.
    """

    game, rounds = line.split(":")
    _, game_number = game.split()
    game_number = int(game_number)

    min_cubes_needed = {}

    for round_ in rounds.split(";"):
        for colour in round_.split(","):
            colour.strip()
            count, colour = colour.split()
            colour = colour.upper()
            min_cubes_needed[colour] = max(min_cubes_needed.get(colour, 0), int(count))

    return game_number, min_cubes_needed


def is_cube_count_exceeded(available_cubes, min_cubes_needed):
    for colour, max_count in min_cubes_needed.items():
        if max_count > available_cubes.get(colour, 0):
            return True
    return False


def get_total_power_of_games(results_log):
    power_levels = []
    with open(f"day_2/inputs/{results_log}") as results:
        for line in results:
            _, min_cubes_needed = parse_line(line)
            power_levels.append(calculate_power(min_cubes_needed))
    return sum(power_levels)


class PowerLevelExceeded(ValueError):
    def __init__(self, power_level, message="It's over 9000!!"):
        self.power_level = power_level
        super().__init__(message)


def calculate_power(cubes):
    power = 1
    for cube_count in cubes.values():
        power *= cube_count
    if power > 9000:
        raise PowerLevelExceeded(power, "It's over 9000!!!")
    return power


if __name__ == "__main__":
    cubes_in_game = {"RED": 12, "GREEN": 13, "BLUE": 14}
    possible_games = tuple(get_possible_games("challenge.txt", cubes_in_game))
    print(sum(possible_games))

    try:
        print(get_total_power_of_games("challenge.txt"))
    except PowerLevelExceeded as exc:
        print(exc.power_level)
