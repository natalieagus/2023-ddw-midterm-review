from mergesort import merge_sort


def test_merge_sort_empty_list():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]


def test_merge_sort_two_sorted_elements():
    assert merge_sort([1, 2]) == [1, 2]


def test_merge_sort_two_reversed_elements():
    assert merge_sort([2, 1]) == [1, 2]


def test_merge_sort_multiple_unsorted_elements():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_duplicate_elements():
    assert merge_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]


def test_merge_sort_large_list():
    assert merge_sort(list(range(100, 0, -1))) == list(range(1, 101))


def test_merge_sort_strings():
    assert merge_sort(["apple", "banana", "cherry", "date"]) == [
        "apple", "banana", "cherry", "date"]


def test_merge_sort_mixed_case_strings():
    assert merge_sort(["apple", "Banana", "cherry", "Date"]) == [
        "Banana", "Date", "apple", "cherry"]
