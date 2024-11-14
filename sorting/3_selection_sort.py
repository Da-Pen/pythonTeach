# Idea: find the smallest element of the list and put it at index 0.
#       Then find the second smallest element and put it at index 1.
#       Then find the third smallest element and put it at index 2.
#       ...
#       Continue until you've found the (n-1)th smallest element (for
#           a list of n items)
def selection_sort(l):
    for i in range(len(l) - 1):
        min_index = i
        for j in range(i + 1, len(l)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]


my_list = [3, 4, 1, -9, 18, 26, 0, 6, -1]
selection_sort(my_list)
print(my_list)