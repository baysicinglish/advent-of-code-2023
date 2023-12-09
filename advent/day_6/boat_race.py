

def calculate_records_margins_for_error(records_file):
    with open(f"day_6/inputs/{records_file}", "r") as records:
        _, *times = records.readline().split()
        _, *distances = records.readline().split()

    times, distances = [int(time) for time in times], [int(distance) for distance in distances]
    records = list(zip(times, distances))

    margins_for_error = []
    for record in records:
        times = calculate_winning_charge_times(record)
        margins_for_error.append(len(times))

    margin_sum = 1
    for margin in margins_for_error:
        margin_sum *= margin

    return margin_sum


def calculate_winning_charge_times(record):
    winning_charge_times = []

    time, distance = record
    for charge_time in range(time):
        potential_distance = charge_time * (time - charge_time)
        if potential_distance > distance:
            winning_charge_times.append(charge_time)

    return winning_charge_times


if __name__ == "__main__":
    print(calculate_records_margins_for_error("challenge.txt"))
