# Idea: TODO
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


my_list = [3, 4, 1, -9, 18, 26, 0, 6, -1]
bubble_sort(my_list)
print(my_list)