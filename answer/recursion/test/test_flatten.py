from flatten import flatten_nested_list
import pytest

# Define test cases for the flatten_nested_list function
test_cases = [
    ([1, [2, [3, 4], 5], 6], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, [2, [3, [4, [5]]]], 6], [1, 2, 3, 4, 5, 6]),
    ([], []),
]

# Create parametrized tests using the test cases


@pytest.mark.parametrize("input_list, expected_output", test_cases)
def test_flatten_nested_list(input_list, expected_output):
    result = flatten_nested_list(input_list)
    assert result == expected_output


# Run the tests
if __name__ == '__main__':
    pytest.main()
