
# Create a hard-coded 2D list
my_2d_list = [
    [2, 5, 6],
    [4, 7, 1],
    [3, 11, 10],
    [8, 9, 0]
]

# 2D list access
val = my_2d_list[2][1]
print(val)  # What will this be?

# NOTE which coordinate comes first? It's a bit different from Cartesian plane!
# Exercises: what will these print?
# print(my_2d_list[0][1])
# print(my_2d_list[-1][2])
# print(my_2d_list[2][1])

# Explain that the length of all rows will generally be the same

# Iterating through a 2D list
# for row in my_2d_list:
#     for col in row:
#         print(col, end="\t")
#     print()  # print newline

# Exercise: write a function that takes a 2D list and a number and counts the number
#       of occurrences of that number in the 2D list

# Exercise: write a function that takes a 2D list and two numbers and replaces all
#       occurrences of the first number with the second number

# Exercise: Write a function that takes a 2D list and returns a new list where each
#       element is the sum of that given row
#       ex. sum_rows([[2, 3], [5, 6], [1, 0]]) => [5, 11, 1]

# Exercise: Write a function that takes a 2D list and returns a new list where each
#       element is the sum of that given column
#       ex. sum_cols([[2, 3], [5, 6], [1, 0]]) => [8, 9]

# Exercise: Write a function that takes a 2D list and returns the sum of the outer border
#       ex. sum_border([
#           [1, 0, 0, 1],
#           [2, 3, 4, 2],
#           [4, 3, 2, 1]
#       ]) => 16

# Exercise: Write a function that takes a number n and returns a nxn grid where the diagonal
#   (from top left to bottom right) is filled with 1's, and all other numbers are 0's
#   ex. if n = 4, returns  [[1, 0, 0, 0],
#                           [0, 1, 0, 0],
#                           [0, 0, 1, 0],
#                           [0, 0, 0, 1]]

# Exercise: Write a function that takes a number n and returns a nxn checkerboard of 0's and 1's
#   ex. if n = 4, returns  [[0, 1, 0, 1],
#                           [1, 0, 1, 0],
#                           [0, 1, 0, 1],
#                           [1, 0, 1, 0]]

# Exercise: Write a function that takes a 2D list and rotates it by 90 degrees clockwise
#   ex. rotate_90([[1, 2, 3],
#                  [4, 5, 6]])
#       would return [[4, 1],
#                     [5, 2],
#                     [6, 3]]

# Exercise: Word Search: Write a function that takes a grid of characters and a word
#   and determines if the word can be found horizontally or vertically in the grid.
#   You can assume that it is going rightwards or downwards.
#   Part 2: Instead of returning True or False:
#       If the word can be found, return the starting position of the word and "vertical" or "horizontal"
#       If the word cannot be found, return None
#   Part 3: Modify it so that the word can also be backwards
#   Part 4 (advanced): Modify it so that the word can also be diagonal (in any direction)
#   Part 5 (super advanced): The word can "curve", i.e. direction can change in the middle of the word


# Alternative ways to create 2D lists
one_dimensional_list = [0] * 5
two_dimensional_list = [[0] * 5] * 10

# Create 2D list with list comprehension
two_dimensional_list_from_comprehension = [[0 for _ in range(5)] for _ in range(10)]

# Create a 2D list where each element is the tuple (row, col)
two_dimensional_list_of_positions = [[(y, x) for x in range(5)] for y in range(10)]
