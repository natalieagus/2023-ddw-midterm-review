from factorial import calculate_factorial


def test_factorial_of_zero():
    result = calculate_factorial(0)
    assert result == 1


def test_factorial_of_positive_number():
    result = calculate_factorial(5)
    assert result == 120


def test_factorial_of_negative_number():
    result = calculate_factorial(-3)
    assert result is None
