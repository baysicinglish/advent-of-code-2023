

def calculate_scratchcard_points(scratchcard_table):
    with open(f"day_4/inputs/{scratchcard_table}", "r") as table:
        for row in table:
            _, numbers = row.split(":")
            winning_numbers, revealed_numbers = [set(subset.strip().split()) for subset in numbers.split("|")]
            matches = revealed_numbers.intersection(winning_numbers)

            yield 1 * 2 ** (len(matches) - 1) if matches else 0


if __name__ == "__main__":
    scores = tuple(calculate_scratchcard_points("challenge.txt"))
    print(sum(scores))
