
# break
# Example: look for the first occurrence of 0 in a list of numbers
numbers = [5, 2, 3, 0, 7, 9, 0, 3]
for i in range(len(numbers)):
    print(numbers[i])
    if numbers[i] == 0:
        print("The first occurrence of 0, is at index", i)
        break

# Example: print messages from the user until they type "stop"
while True:
    message = input('Type a message (or "stop" to exit): ')
    if message == "stop":
        break
    print("Your message was:", message)

# continue
# Task: A list has numbers mixed in with None's. Get the sum of all the numbers.
# ex. [3, 5, -4, None, 2, -1, None] => 5
nums = [3, 5, -4, None, 2, -1, None]
sum = 0
for num in nums:
    if num is None:
        continue
    print("Adding", num, "...")
    sum += num

print(sum)

# Exercise: Create a function first_even_and_odd_number(l) that takes a list of numbers
#           and prints the first even number in the list, then prints the first odd number
#           in the list. You can assume that there is at least one even number and at
#           least one odd number.

# Exercise: Create a function called sum_of_valid_lists(l) that takes a list of list of numbers
#           and returns the sum of all numbers in all valid lists. For this question, a list is
#           considered valid only if it does NOT contain None.
#           Ex. sum_of_all_valid_lists([[3, 4, -1, 0], [0, None, 2, 3], [3, 1]]) => 10