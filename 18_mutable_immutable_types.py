# Immutable data types in Python can't change. They include:
#  - int
#  - float
#  - bool
#  - string
#  - tuple
#  - Complex, Stringfrozen set, Bytes (won't learn)

# Mutable data types in Python can change. They include EVERYTHING ELSE. Including:
#  - list
#  - dict
#  - set
#  - Objects
#  - ...

# What do I mean by "can't change"? For example, we can do
x = 3
x += 1
print(x)  # prints 4

# Didn't x change?
# We need to differentiate between a variable and a value.
# x is a variable, it refers to a value. When we do x += 1, we change it to refer to a different value.
# But we don't update the value itself, because it is immutable.
# Contrast that with this:

l = [1, 2, 3]
l.append(4)
print(l)

# Here, l is a variable that refers to the value [1, 2, 3].
# Then, when we append 4 to the list, we actually update the value itself,
# while l still refers to that same value.

# This should explain all the behaviour we see above.