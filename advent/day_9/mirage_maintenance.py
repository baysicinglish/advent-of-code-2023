

def predict_environmental_conditions(oasis_report):
    conditions = []

    with open(f"day_9/inputs/{oasis_report}", "r") as recordings:
        for values in recordings:
            readings = [int(value) for value in values.strip().split()]
            conditions.append(readings)

    forecast = []

    for condition in conditions:
        forecast.append(predict_future_value(condition))

    return sum(forecast)


def predict_future_value(history):
    if all([value - history[-1] == 0 for value in history]):
        return history[-1]

    changes = []
    for reading_number in range(1, len(history)):
        change = history[reading_number] - history[reading_number - 1]
        changes.append(change)

    return history[-1] + predict_future_value(changes)


if __name__ == "__main__":
    print(predict_environmental_conditions("challenge.txt"))
