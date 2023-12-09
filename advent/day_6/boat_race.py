from typing import Iterable


def calculate_total_margin_for_error_for_all_records(records_file):
    with open(f"day_6/inputs/{records_file}", "r") as records:
        _, *times = records.readline().split()
        _, *distances = records.readline().split()

    times, distances = [int(time) for time in times], [int(distance) for distance in distances]
    records = list(zip(times, distances))

    margins_for_error = [calculate_margin_for_error(record) for record in records]

    return calculate_product(margins_for_error)


def calculate_margin_for_error_from_record(records_file):
    with open(f"day_6/inputs/{records_file}", "r") as records:
        time = int("".join(records.readline().split()[1:]))
        distance = int("".join(records.readline().split()[1:]))

    record = (time, distance)

    return calculate_margin_for_error(record)


def calculate_margin_for_error(record):
    time = record[0]

    fastest_time = calculate_fastest_winning_charge_time(record)
    slowest_time = time - fastest_time

    return slowest_time - fastest_time + 1


def calculate_fastest_winning_charge_time(record):
    time, distance = record

    for charge_time in range(time):
        potential_distance = charge_time * (time - charge_time)
        if potential_distance > distance:
            return charge_time


def calculate_product(numbers: Iterable[int]):
    total_sum = 1
    for number in numbers:
        total_sum *= number

    return total_sum


if __name__ == "__main__":
    print(calculate_total_margin_for_error_for_all_records("challenge.txt"))
    print(calculate_margin_for_error_from_record("challenge.txt"))
