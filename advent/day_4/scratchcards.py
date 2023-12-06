

def get_scratchcard_matches(scratchcard):
    _, numbers = scratchcard.split(":")
    winning_numbers, revealed_numbers = [set(subset.strip().split()) for subset in numbers.split("|")]
    return revealed_numbers.intersection(winning_numbers)


def calculate_scratchcard_points(scratchcard_table):
    with open(f"day_4/inputs/{scratchcard_table}", "r") as table:
        for scratchcard in table:
            matches = get_scratchcard_matches(scratchcard)

            yield 1 * 2 ** (len(matches) - 1) if matches else 0


def calculate_total_scratchcards(scratchcard_table):
    with open(f"day_4/inputs/{scratchcard_table}", "r") as table:
        scratchcard_count = 0
        queue = [1]

        for scratchcard in table:
            num_copies = get_copy_count(queue)
            scratchcard_count += num_copies
            matches = get_scratchcard_matches(scratchcard)
            for index in range(len(matches)):
                add_copies_to_queue(queue, index, num_copies)

    return scratchcard_count


def get_copy_count(queue):
    try:
        return queue.pop(0)
    except IndexError:
        return 1


def add_copies_to_queue(queue, index, count):
    while len(queue) <= index:
        queue.append(1)

    queue[index] += count


if __name__ == "__main__":
    scores = tuple(calculate_scratchcard_points("challenge.txt"))
    print(sum(scores))

    num_scratchcards = calculate_total_scratchcards("challenge.txt")
    print(num_scratchcards)
