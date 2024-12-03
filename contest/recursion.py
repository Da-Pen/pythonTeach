# Recursion is when a function calls itself.


# Example: Factorial calculator
# Solution using iteration:
def factorial_iteration(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

print(factorial_iteration(5))


# Solution using recursion:
def factorial_recursion(n):
    if n == 1:  # base case
        return 1
    return n * factorial_recursion(n - 1)

print(factorial_recursion(5))

# VOCABULARY:
#  - Recursion: when you use a function that calls itself
#  - Iteration: when you use loops
#  - Base Case: the case when a recursive function doesn't call itself

# Question: How are recursion and iteration similar?

# Note: ANY problem that can be solved with recursion can be solved with iteration,
#   and ANY problem that can be solved with iteration can be solved with recursion.
#   Pick the strategy that results in a simpler solution. In some cases it is recursion,
#   in some cases it is iteration.

# Question: what happens if there is no base case in a recursive function?

# Question: what is the base case in a recursive function similar to in a while loop?
# Question: what is the base case in a recursive function similar to in a for loop?

# Example: count digits of a positive integer (without using log function)
def count_digits_iteration(n):
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return digits

print(count_digits_iteration(12345))


def count_digits_recursion(n):
    if n == 0:
        return 0
    return 1 + count_digits_iteration(n // 10)

print(count_digits_iteration(12345))


# Example: check whether a string is a palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("abccba"))
print(is_palindrome("abcba"))
print(is_palindrome("abca"))


# TWO-BRANCH RECURSION

# Example: Get the n-th Fibonacci number.
# What is the Fibonacci sequence?
# Start with 1, 1 and each next number is the sum of prev two numbers:
#   1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Fun fact: the Fibonacci Sequence is observed in nature. For example:
#   - The number of petals on a flower is usually a Fibonacci number
#   - Many spiral shells, like the shell of a nautilus, grows in a shape that approximates the Fib. sequence

def fibonacci_sequence_iteration(n):
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

print(fibonacci_sequence_iteration(7))


def fibonacci_sequence_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_sequence_recursion(n - 1) + fibonacci_sequence_recursion(n - 2)

print(fibonacci_sequence_recursion(7))

# Explain why it's "two-branch" recursion
# Note: there can be more than two branches!


# Example: Binary search
# Say you have a sorted list, and you want to check if a number exists in the list.
#   Ex. if you have the list l=[1, 4, 7, 12, 13, 25, 40] and target=25
#       How would you do it? How would you do it efficiently?

def binary_search(l, target):
    if len(l) == 0:  # Base case: Target not found
        return False

    mid = len(l) // 2  # Find the middle index
    if l[mid] == target:
        return True  # Target found
    elif l[mid] < target:
        return binary_search(l[mid + 1:], target)  # Search in the right half
    else:
        return binary_search(l[:mid], target)  # Search in the left half

print(binary_search([1, 4, 7, 12, 13, 25, 40], 25))

# Explain why it's called binary search
# Question: is this one-branch or two-branch recursion?

# Binary search that returns index
# Question: what is the problem with the previous binary search? Why can't it return the index?
# Solution:
def binary_search_return_index_helper(l, target, start, end):
    if start >= end:  # Base case: Target not found
        return None

    mid = (end + start) // 2  # Find the middle index
    if l[mid] == target:
        return mid  # Target found
    elif l[mid] < target:
        return binary_search_return_index_helper(l, target, mid + 1, end)  # Search in the right half
    else:
        return binary_search_return_index_helper(l, target, start, mid)  # Search in the left half


def binary_search_return_index(l, target):
    return binary_search_return_index_helper(l, target, 0, len(l))


print(binary_search_return_index([1, 4, 7, 12, 13, 25, 40], 25))

# Explain idea of helper function


# Exercise: Write a function that returns the sum of all elements of an array (without using any loops or the sum() function)
# Exercise: Write a function that takes a string as input and returns the reverse of the string
# Exercise: Count the number of vowels in a string
