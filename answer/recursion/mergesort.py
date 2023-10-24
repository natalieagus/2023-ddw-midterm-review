def merge_sort(arr):
    # Step 1: Base case
    if len(arr) <= 1:
        return arr

    # Step 2: Divide the array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Step 4: Compare and merge the elements from both halves
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Step 5: Handle any remaining elements in left and right
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


# Step 6: Example usage
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)
