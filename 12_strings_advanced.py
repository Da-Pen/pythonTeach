# string formatting with f-strings
name = "Daniel"
age = 25
s = f"Hi, my name is {name} and I am {age} years old"
print(s)

# special characters
s = "This is a string\nOn two separate lines"
print(s)
s = "This is a string with a\ttab in between"
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
