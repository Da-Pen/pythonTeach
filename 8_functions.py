# INTRODUCTION: provide a few example of machines and describe the input / output, then examine what the machine is
#   doing with the input / output. Give them some examples and ask them what input / output is
#   Machines:
#       - Microwave: food, time -> hotter food
#       - Washing Machine: clothes, soap, dirt level, spin level -> clean clothes
#       - Vending Machine: number, money -> item
#       - Water Fountain: (no input, just "run it") -> Water
#       - Wind-up Music Box OR Car Horn: (no input, just "run it") -> music and visuals (no return, just "side effect")

# Example
# Function Definition
def multiply_numbers(x, y):  # explain parameters: they're like variables that only exist in the function
    return x * y

# Using the function (also called "calling" the function)
product = multiply_numbers(4, 3)
print(product)
product = multiply_numbers(-5, 7)
print(product)

num1 = 5
num2 = 6
product = multiply_numbers(num1, num2)
print(product)

# Exercises
# - Write a function that takes the length and width of a rectangle and returns the perimeter. Test it with a few
#   different test cases.
# - Write a function that takes a name and prints "hi {name}!" 3 times.
# - Write a function that takes a name, prints the name, and returns the length of the name.
# - Write a function that takes three numbers and returns True if they are in order
#   (first number is the smallest, then second, then third).
# - Write a function that takes a number n and a message and prints that message n times.
# - Write a function that keeps asking for a message from a user until they type "stop". Return the number of messages
#   they gave.
# - Write a function sum_of_evens(n) that returns the sum of all even numbers from 2 to n.
# - Write a function sum_of_digits(n) that takes an integer n and returns the sum of its digits.
# - Write a function count_vowels(s) that takes a string and returns the number of vowels in the string.
# - Write a function is_prime(num) that takes a number and returns True if the number is prime and False otherwise.
# - Write a function factorial(n) that calculates and returns the factorial of a given number. The factorial of n is the
#   product of all positive integers less than or equal to n (ex. 5! = 5 * 4 * 3 * 2 * 1).
# - Write a function find_largest(a, b, c) that takes three numbers as arguments and returns the largest of the three.
#   Use if statements to make the comparison.

# Longer Exercise:
# Part 1: ask the user for a number n from 1-9 and print that number n times in one line (hint: use print(n, end=''))
# Part 2: print a square of that number. Ex. if the user enters 3, print:
#           333
#           333
#           333
# Part 3: print a diagonal line. Ex. if the user enters 3, print:
#           3
#            3
#             3
# Part 4: can repeat the code (ex. ask user for number then print the square, then ask user for another number, etc.)
