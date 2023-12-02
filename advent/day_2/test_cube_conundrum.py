import pytest

from .cube_conundrum import (
    get_possible_games,
    parse_line,
    is_cube_count_exceeded,
    get_total_power_of_games,
    calculate_power,
    PowerLevelExceeded,
)


class TestGetPossibleGames:
    def test_returns_ids_of_possible_games(self):
        available_colours = {
            "RED": 12,
            "GREEN": 13,
            "BLUE": 14
        }

        possible_games = get_possible_games("example.txt", available_colours)

        assert tuple(possible_games) == (1, 2, 5)


class TestParseLine:
    def test_returns_number_and_min_cubes_needed(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

        game_number, revealed_colours = parse_line(line)

        assert game_number == 1
        assert revealed_colours == {
            "BLUE": 6,
            "RED": 4,
            "GREEN": 2
        }

    def test_returns_multiple_digit_game_number(self):
        line = "Game 100: 3 blue, 4 red"

        game_number, _ = parse_line(line)

        assert game_number == 100


class TestIsCubeCountExceeded:
    def test_cube_count_not_exceeded_returns_false(self):
        available_cubes = {'RED': 4, 'GREEN': 13, 'BLUE': 14}
        min_game_cubes = {'BLUE': 6, 'RED': 4, 'GREEN': 2}

        result = is_cube_count_exceeded(available_cubes, min_game_cubes)

        assert result is False

    def test_cube_count_exceeded_returns_true(self):
        available_cubes = {'RED': 12, 'GREEN': 13, 'BLUE': 14}
        min_game_cubes = {'BLUE': 6, 'RED': 20, 'GREEN': 13}

        result = is_cube_count_exceeded(available_cubes, min_game_cubes)

        assert result is True

    def test_unexpected_cube_colour_returns_true(self):
        available_cubes = {'RED': 5}
        min_game_cubes = {'RED': 4, 'BLACK': 1}

        result = is_cube_count_exceeded(available_cubes, min_game_cubes)

        assert result is True


class TestGetTotalPowerOfGames:
    def test_calculates_total_power(self):
        power = get_total_power_of_games("example.txt")

        assert power <= 9000
        assert power == 2286


class TestCalculatePower:
    def test_raises_exception_if_power_over_9000(self):
        cubes = {"RED": 9001}

        with pytest.raises(PowerLevelExceeded):
            calculate_power(cubes)
