from .seeds import remove_range_overlap


def test_remove_range_overlap():
    ranges = {1: 7, 4: 10, 40: 50, 80: 100, 90: 100}

    distinct_ranges = remove_range_overlap(ranges)

    assert distinct_ranges == {1: 7, 7: 10, 40: 50, 80: 100, 100: 100}
