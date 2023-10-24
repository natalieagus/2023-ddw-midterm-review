# Import the function
# Replace 'your_module' with the actual name of your module
from geo_seq import geometric_sequence_term


def test_geometric_sequence_term_first_term():
    a = 2
    r = 3
    n = 1
    result = geometric_sequence_term(a, r, n)
    assert result == a


def test_geometric_sequence_term_nth_term():
    a = 2
    r = 3
    n = 4
    result = geometric_sequence_term(a, r, n)
    expected_result = a * (r ** (n - 1))
    assert result == expected_result


def test_geometric_sequence_term_zeroth_term():
    a = 2
    r = 3
    n = 0
    result = geometric_sequence_term(a, r, n)
    assert result == None  # The function returns None for n < 1


def test_geometric_sequence_term_negative_n():
    a = 2
    r = 3
    n = -2
    result = geometric_sequence_term(a, r, n)
    assert result == None  # The function returns None for n < 1
