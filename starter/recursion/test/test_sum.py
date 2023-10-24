# Import the function
from sum_recursive import recursive_sum


def test_recursive_sum_empty_list():
    lst = []
    result = recursive_sum(lst)
    assert result == 0


def test_recursive_sum_single_element():
    lst = [5]
    result = recursive_sum(lst)
    assert result == 5


def test_recursive_sum_positive_numbers():
    lst = [1, 2, 3, 4, 5]
    result = recursive_sum(lst)
    expected_result = sum(lst)
    assert result == expected_result


def test_recursive_sum_mixed_numbers():
    lst = [-2, 4, -1, 6, -3]
    result = recursive_sum(lst)
    expected_result = sum(lst)
    assert result == expected_result


def test_recursive_sum_nested_lists():
    lst = [1, [2, 3, [4, 5], 6], [7, 8]]
    result = recursive_sum(lst)
    expected_result = sum([1, 2, 3, 4, 5, 6, 7, 8])
    assert result == expected_result
