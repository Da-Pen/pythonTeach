# To learn sorting, should be familiar with:
# - Nested loops
# - Recursion (for merge sort)


# NESTED LOOPS EXERCISES

# Write a function that, given a number n, prints the following with n rows:
# *
# * *
# * * *
# * * * *
# * * * * *

# Write a function that prints a 10x10 multiplication table
# Solution:
def print_multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()

# Write a function that returns the first n rows of Pascal's Triangle.
# Pascal's Triangle looks like this:
#
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#  1 5 10 10 5 1
# 1 6 15 20 15 6 1
#       ...
#
# Solution:
def pascals_triangle(n):
    l = [[1]]
    for i in range(1, n):
        new_row = [1] * (i+1)
        for j in range(1, i):
            new_row[j] = l[i - 1][j - 1] + l[i - 1][j]
        l.append(new_row)
    return l

# print(pascals_triangle(10))

