# Motivating example: If I want to keep track of LeBron's PPG in different games.
#  How would I do that (without a list)? How would I print all the scores?

# Now with a list:
points_per_game = [15, 30, 22, 11, 7, 8, 12]  # create a list
# print(points_per_game)  # print the list
# print(len(points_per_game))  # print the length of the list

# Other examples of lists
students = ["Emily", "Steven", "Jared"]
electricity_bill_payments = [80.8, 96.45, 79.98, 88.1]
attended_class = [True, True, False, True, True]
mixed_list = ["abcd", 80, 2.0, False]  # can have different variable types, but usually they are all the same
homework_completed = []
list_of_lists = [[1, 2, 3], [], [4, 5], [6]]

# exercise: create a list of 5 foods that you like
# exercise: create a list of the first 8 perfect squares

# points_per_game = [15, 30, 22, 11, 7, 8, 12]

# get list element or sublist
# explain that lists are 0-indexed
# print(points_per_game[1])
# print(points_per_game[-1])
# print(points_per_game[2:5])
# print(points_per_game[2:])
# print(points_per_game[:5])
# print(points_per_game[15])  # IndexError: list index out of range

# some simple exercises (ex. get the nth item, the nth last item, the nth to mth sublist)
# exercise: print every item in a list using a for loop (without for each loop)

# do something with every item in a list
# for points_in_game in points_per_game:
#     print(points_in_game)

# update value of an item in a list
# points_per_game[1] = 40
# print(points_per_game)
# exercise: update the 16 in the list to 12

# append
# points_per_game.append(40)
# print(points_per_game)

# remove an item
# print(points_per_game)
# points_per_game.remove(15)
# points_per_game.remove(40)  # duplicated item
# print(points_per_game)

# sort list
# print(points_per_game)
# points_per_game.sort()
# print(points_per_game)

# try to update elements in a list
# for points in points_per_game:
#     points += 1
# print(points_per_game)

# correct way to do it
# for i in range(len(points_per_game)):
#     points_per_game[i] += 1
# print(points_per_game)


# Check if an item is in a list
got_15_points = 15 in points_per_game
print(got_15_points)
got_14_points = 14 in points_per_game
print(got_14_points)

# exercises: review each of the list operations individually:
#  - List creation, get length, get items by index (including counting from end), get sublist, update value by index,
#    append to list, remove item, sort

# Multipart exercise: max, sum, and average calculator
#  (1) create a list with the following numbers: 10, 2, 4, 8, 6, 6, 12, 5
#  (2) write a function sum(l) that returns the sum of the values in the list
#  (3) write a function max(l) that returns the max value of the list without sorting
#  (4) write a function max_by_sorting(l) to get the max value of the list by sorting it first
#  (5) write a function average(l) that gets the average value of the list (hint: average(l) should call sum(l))
#  (6) now change it to ask the user for a list of numbers. Start with an empty list and keep asking for numbers until
#      the user types "stop"
#  (7) [challenge] get the median of the list

