from .mirage_maintenance import predict_environmental_conditions, extrapolate_value


class TestPredictEnvironmentalConditions:
    def test_predicts_example_total_change(self):
        predicted_change = predict_environmental_conditions("example.txt")

        assert predicted_change == 114

    def test_predicts_example_total_previous_change(self):
        predicted_change = predict_environmental_conditions("example.txt", reverse=True)

        assert predicted_change == 2


class TestExtrapolateValue:
    def test_predicts_condition_change(self):
        history = [10, 13, 16, 21, 30, 45]

        predicted_value = extrapolate_value(history)

        assert predicted_value == 68

    def test_predicts_previous_condition_change(self):
        known_history = [10, 13, 16, 21, 30, 45]

        predicted_value = extrapolate_value(known_history, reverse=True)

        assert predicted_value == 5
