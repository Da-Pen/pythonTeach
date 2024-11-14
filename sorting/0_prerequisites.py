# To learn sorting, should be familiar with:
# - Nested loops


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

# Write a function that prints the first n rows of Pascal's Triangle.
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
# Don't worry about formatting the output (i.e. lining up horizontally). Your output will look like:
# 1
# 1 1
# 1 2 1
# ...




