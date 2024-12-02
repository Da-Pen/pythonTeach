
def merge(left_list, right_list):
    sorted_list = []
    left_index = 0
    right_index = 0

    # Compare elements from left and right, adding the smallest to the sorted array
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    # Add any remaining elements from the left or right half
    for i in range(left_index, len(left_list)):
        sorted_list.append(left_list[i])
    for i in range(right_index, len(right_list)):
        sorted_list.append(right_list[i])

    return sorted_list


def merge_sort(l):
    if len(l) <= 1:
        return l

    # Divide the array into two halves
    mid = len(l) // 2
    left_half = l[:mid]
    right_half = l[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


l = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(l))
