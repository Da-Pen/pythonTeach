# string formatting with f-strings
name = "Daniel"
age = 25
s = f"Hi, my name is {name} and I am turning {age + 1} years old next year"
print(s)

# special characters
s = "This is a string\nOn two separate lines"
print(s)
s = "This is a string\twith some\ttabs in between"
print(s)

multiline_string = '''This is
a string
on multiple lines'''
print(multiline_string)

# What if we wanted to format the previous string? Show what would happen.
multiline_string_2 = "This is" \
                     "\nanother string" \
                     "\non multiple lines"
print(multiline_string_2)

# join and split
my_pets = ["Ralph", "Max", "Whiskers"]
my_pets_joined = ", ".join(my_pets)
print("My pets are", my_pets_joined)

file_path = "C:/Users/Daniel/Documents/School/Programming/python_projects/my_python_project"
print(file_path.split("/"))

# Using ' and " in strings
# s = 'Why won't this work?'
s = "But this should work, shouldn't it?"

# s = "My name is "Catherine""
s = 'My name is "Catherine"'

# What if I want the string: My cat's name is "Whiskers"?
s = 'My cat\'s name is "Whiskers"'
# OR:
s = "My cat's name is \"Whiskers\""

# Backslash in a string
s = "l\\m\\n\\o\\p"
print(s)

# Exercise: Create a variable to store the string: a\\b"b'b'\c	bd
#           Note: there is a tab between the c and the last b
#           Then use that string to create a list containing the elements:
#           a\\, ", ', '\c	, and d

# Exercise: how would I write an f-string that says "My mark in [class] is [mark]"
#           if I have my mark and class stored in variables?


# strings as a list of characters
s = 'abcdefghijk'
print(s[3])
print(s[-2])
print(s[3:-2])
for letter in s:
    print(letter)
