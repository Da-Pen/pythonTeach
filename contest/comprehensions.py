# Comprehensions are shorter ways to construct new lists, tuples, dictionaries, and sets.

# List comprehension
# Example: Let's say we want to take a list of numbers and get a new list with the same
# numbers except doubled. Without list comprehension we would do it like this:
l = [1, 2, 3, 4, 5, 6]
l_doubled = []
for num in l:
    l_doubled.append(num * 2)

# With list comprehension we can do it like this:
l_doubled = [num * 2 for num in l]

# Example: Let's say we want to take a list of numbers and get a new list with only the
# even numbers. Without List comprehension we would do it like this:
l = [1, 2, 3, 4, 5, 6]
l_evens = []
for num in l:
    if num % 2 == 0:
        l_evens.append(num)

# With list comprehension we can do it like this:
l_evens = [num for num in l if num % 2 == 0]

# Exercises: what do these print?
l = [1, 2, 3, 4, 5, 6]
print([num ** 2 for num in l])
print([num - 1 for num in l if num % 3 == 0])
print([num for num in range(10)])
print([num ** 3 for num in range(10)])
print([num for num in range(10, 30, 2)])
text = "24 35 66 1 -50"
print([int(num) for num in text.split(" ")])

# Exercise: Create a list of the first 10 perfect squares
# Challenge: Given a list of numbers, create a new list with only the numbers
#       at even indices of the original list
#       Ex. [55, 6, 12, 84, 0, 12] -> [55, 12, 0]

# Example: 2D list with list comprehension
# Create a 10x10 2D list with all 0's
l = [[0 for i in range(10)] for j in range(10)]
print(l)

# Exercise: Create a 10x10 2D list where each element is the product of the indices
# Exercise: Given a list of numbers as well as a number n, create a list of all numbers from 1 to n (inclusive)
#       that are NOT in the given list
# Exercise: Write a function that takes a string as input and returns the reverse of the string
# Exercise: Count the number of vowels in a string


# Set Comprehension
# Example: Create a set of all words that start with g in a sentence
sentence = "Golden geese grazed peacefully near the old garden gate"
g_words = {word for word in sentence.lower().split() if word[0] == 'g'}
print(g_words)

# Exercise: create a set of all letters that appear in a string
# Exercise: given a map from student names to mark, create a set of all failing
#   students (mark lower than 50).
# Exercise: Write a function that takes a dictionary that maps student names to marks
#   and returns create a set of tuples (name, mark) of all failing students (mark < 50)
#   Ex. failing_students({"DeMar": 35, "Trae": 46, "Luka": 50, "Giannis": 99}) should
#       return the set {("DeMar", 35), ("Trae", 46)}


# Tuple comprehension
# Example: given a tuple of numbers, create another tuple of the squares
#   of all positive numbers in the tuple
t = (3, -4, 6, 4, -8)
print(tuple(num ** 2 for num in t if num > 0))

# More details, unnecessary to explain but writing them here as a note:
# Caveat: There is technically no "tuple comprehension", it is actually a generator
#   comprehension that we convert to a tuple. A generator is a lazily-evaluated iterable
#   object. Generators are used instead of tuples for efficiency reasons.
# Example:
g = (n ** 1000 for n in range(10000))  # creates a generator, runs fast because items are not evaluated
# print("Done creating generator")
# print(tuple(g))  # slow because all items have to be evaluated to be converted into a tuple

# Example: Given a list of words, create a tuple of words with only the vowels from each word
l = ["hello", "it's", "me", "i've", "been", "wondering", "if", "after", "all", "these"]

def only_vowels(s):
    return ''.join(letter for letter in s if letter in 'aeiou')

print(tuple(only_vowels(s) for s in l))

# Exercise: given a list of strings, create a tuple of the lengths of the strings


# Dictionary Comprehension
# Example: given a list of numbers, create a dictionary where the key is the number and
# the value is the cube of the number. Without dictionary comprehension:
l = [1, 3, 6, 8]
nums_cubed = {}
for num in l:
    nums_cubed[num] = num ** 3

# With dictionary comprehension:
nums_cubed = {num: num ** 3 for num in l}
print(nums_cubed)

# Example: Given a list of words, create a dictionary from word to length of word for all
#          words that start with "g" (capital or lowercase)
sentence = "Golden geese grazed peacefully near the old garden gate"
word_lengths = {word: len(word) for word in sentence.split() if word[0] in ('g', 'G')}
print(word_lengths)

# Exercise: given a dictionary mapping student ID to student name, and student ID to mark,
#       create a new dictionary mapping student name to mark
#       ex. id_to_name {3: "Spongebob S", 6: "Patrick S", 11: "Squidward T"}
#           id_to_grade {3: 65, 6: 45, 11: 99}
#           you should generate {"Spongebob S": 65, "Patrick S": 45, "Squidward T": 99}

