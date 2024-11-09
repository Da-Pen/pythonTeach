# Motivating example: get all unique words in a sentence
sentence = "The man we saw saw a man who saw a saw"
list_of_words = sentence.split(" ")
print(list_of_words)

set_of_words = set()
for word in list_of_words:
    set_of_words.add(word)
print(set_of_words)

# Explain that sets are unordered

# Set literal
my_pets = {"cat", "dog", "dog", "cat", "rabbit"}
print(my_pets)

# easier way: directly convert list to set
set_of_words = set(list_of_words)
print(set_of_words)

# Loop over a set
for word in set_of_words:
    print(word)

# Check if an item is in a set
saw_in_set = "saw" in set_of_words
print(saw_in_set)
see_in_set = "see" in set_of_words
print(see_in_set)

# remove an item from a set
set_of_words.remove("saw")
print(set_of_words)

# advanced sets: joining two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s2.difference(s1))

# Other methods that are unnecessary to teach (can use above methods), but for reference:
print(s1.symmetric_difference(s2))  # only items that exist in ONE set
s1.update(s2)  # same as union but updates the first set instead of returning new set
s1.intersection_update(s2)  # same as intersection but updates instead of returning new set
s1.difference_update(s2)  # same as difference but updates instead of returning new set
s1.symmetric_difference_update(s2)  # same as symmetric_difference but updates instead of returning new set

# Exercise: write a function that takes a number n and returns a set of all numbers from 1 to n
# Exercise: write a function that takes a list and returns True if all elements in the list are unique, False otherwise
# Exercise: write a function that takes two lists and returns all the elements that appear in both lists
# Exercise: write a function called missing_numbers(s, n) that takes a set of numbers and a number n and returns a new
#   set containing all the numbers from 1 to n that are NOT in the given set
#       ex. missing_numbers({1, 5, 3}, 6) should return {2, 4, 6}
