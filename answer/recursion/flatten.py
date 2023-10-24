# Implement a recursive function to flatten a nested list.
# Write a Python function called flatten_nested_list that takes a nested list as its argument and returns a flattened list with all elements in a single level.
# The input list may contain other nested lists, and you need to recursively flatten it.
# For example, given the nested list [1, [2, [3, 4], 5], 6], the function should return [1, 2, 3, 4, 5, 6], which is a flattened version of the input list.


def flatten_nested_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    return flattened


# Test the function
nested_list = [1, [2, [3, 4], 5], 6]
result = flatten_nested_list(nested_list)
print(result)
