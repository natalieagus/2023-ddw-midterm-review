# Write a Python function called recursive_sum that takes a list of integers as its argument and returns the sum of all the elements in the list using recursion.

# For example, recursive_sum([1, 2, 3, 4, 5]) should return 15 because the sum of these elements is 1 + 2 + 3 + 4 + 5, which is 15.


def recursive_sum(lst):
    if not lst:  # If the list is empty, return 0
        return 0
    elif isinstance(lst[0], list):  # If the first element is a list, recurse on it
        return recursive_sum(lst[0]) + recursive_sum(lst[1:])
    else:
        # Add the first element and recurse on the rest
        return lst[0] + recursive_sum(lst[1:])


# Test the function
print(recursive_sum([1, 2, 3, 4, 5]))  # Output should be 15
