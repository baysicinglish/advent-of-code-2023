

def get_seed_destinations(almanac):
    with open(f"day_5/inputs/{almanac}", "r") as seed_mappings:
        _, *seeds = seed_mappings.readline().split()
        seeds = [int(seed) for seed in seeds]
        conditions = parse_optimal_condition_mappings(seed_mappings)

    reference_numbers = seeds
    for condition in conditions:
        reference_numbers = map_reference_numbers(reference_numbers, condition)

    return tuple(reference_numbers)


def map_reference_numbers(reference_numbers, mappings):
    for index, reference_number in enumerate(reference_numbers):
        for mapping in mappings:
            if 0 <= (offset := reference_number - mapping["source_start"]) < mapping["range"]:
                reference_numbers[index] = mapping["destination_start"] + offset
                break

    return reference_numbers


def get_closest_seed_destination(almanac):
    with open(f"day_5/inputs/{almanac}", "r") as seed_mappings:
        _, *seeds = seed_mappings.readline().split()

        seeds = [int(seed) for seed in seeds]
        conditions = parse_optimal_condition_mappings(seed_mappings)

    ranges = {seeds[index]: seeds[index] + seeds[index + 1] for index in range(0, len(seeds), 2)}
    distinct_ranges = remove_range_overlap(ranges)    # not sure if this is strictly necessary but it helps

    closest_destination = None
    seed_number = 0

    for lower_bound, upper_bound in distinct_ranges.items():
        seed_number = max(lower_bound, seed_number)

        while seed_number < upper_bound:
            total_skip = float("inf")
            reference_number = seed_number

            # could be nicer as a recursive function
            for mapping_rules in conditions:
                reference_number, skip = map_reference_number_and_skip(reference_number, mapping_rules)
                total_skip = min(skip, total_skip)

            closest_destination = (
                min(closest_destination, reference_number) if closest_destination else reference_number
            )
            seed_number += total_skip if (total_skip and total_skip != float("inf")) else 1

    return closest_destination


def map_reference_number_and_skip(reference_number, mappings):
    for mapping in mappings:
        if 0 <= (offset := reference_number - mapping["source_start"]) < mapping["range"]:
            return mapping["destination_start"] + offset, mapping["range"] + mapping["source_start"] - reference_number

    lower_bound = min(mapping["source_start"] for mapping in mappings)
    skip = lower_bound - reference_number if reference_number < lower_bound else float("inf")
    return reference_number, skip


def parse_optimal_condition_mappings(almanac_data):
    all_mappings = []
    mappings = []

    for line in almanac_data:
        if not (line and line[0].isdigit()):
            if mappings:
                all_mappings.append(mappings)
                mappings = []
                continue

        match line.strip().split():
            case [destination_range_start, source_range_start, range_]:
                mapping = {
                    "destination_start": int(destination_range_start),
                    "source_start": int(source_range_start),
                    "range": int(range_)
                }
                mappings.append(mapping)

    all_mappings.append(mappings)
    return all_mappings


def remove_range_overlap(ranges):
    distinct_ranges = {}
    while ranges:
        min_start_value = min(ranges.keys())
        value = ranges.pop(min_start_value)

        for upper_bound in distinct_ranges.values():
            if min_start_value < upper_bound:
                min_start_value = upper_bound
        distinct_ranges[min_start_value] = value

    return distinct_ranges


if __name__ == "__main__":
    destinations = get_seed_destinations("challenge.txt")
    print(min(destinations))

    print(get_closest_seed_destination("challenge.txt"))
