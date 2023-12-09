from .mirage_maintenance import predict_environmental_conditions, predict_future_value


class TestPredictEnvironmentalConditions:
    def test_predicts_example_total_change(self):
        predicted_change = predict_environmental_conditions("example.txt")

        assert predicted_change == 114


class TestPredictFutureValue:
    def test_predicts_condition_change(self):
        history = [10, 13, 16, 21, 30, 45]

        predicted_value = predict_future_value(history)

        assert predicted_value == 68
