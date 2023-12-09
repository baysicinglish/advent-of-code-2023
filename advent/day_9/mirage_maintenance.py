

def predict_environmental_conditions(oasis_report, reverse=False):
    conditions = []

    with open(f"day_9/inputs/{oasis_report}", "r") as recordings:
        for values in recordings:
            readings = [int(value) for value in values.strip().split()]
            conditions.append(readings)

    forecast = []

    for condition in conditions:
        forecast.append(extrapolate_value(condition, reverse=reverse))

    return sum(forecast)


def extrapolate_value(history, reverse=False):
    index = 0 if reverse else -1

    if all([value - history[index] == 0 for value in history]):
        return history[index]

    changes = []
    for reading_number in range(1, len(history)):
        change = history[reading_number] - history[reading_number - 1]
        changes.append(change)

    predicted_step = extrapolate_value(changes, reverse=reverse)

    if reverse:
        predicted_step *= -1

    return history[index] + predicted_step


if __name__ == "__main__":
    print(predict_environmental_conditions("challenge.txt"))
    print(predict_environmental_conditions("challenge.txt", reverse=True))
