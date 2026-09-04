from flight_calculator import calculate_flight_time, flight_time_table


def test_calculate_flight_time():
    assert calculate_flight_time(100) == 170


def test_calculate_flight_time_zero():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_large_payload():
    assert calculate_flight_time(2000) == 0


def test_calculate_flight_time_negative_weight():
    try:
        calculate_flight_time(-1)
        assert False
    except ValueError:
        assert True


def test_flight_time_table():
    assert flight_time_table(500, 100) == [
        (0, 180),
        (100, 170),
        (200, 160),
        (300, 150),
        (400, 140),
        (500, 130),
    ]
