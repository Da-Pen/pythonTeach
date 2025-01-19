# Review of what we know so far:
true_var = True
false_var = False

if true_var:
    print("a")

if false_var:
    print("b")

if not true_var:
    print("c")

if not false_var:
    print("d")

# What about for non-boolean values?
# Strings, Lists, Sets, Tuples, Dictionaries evaluate to False if they are empty

if not "":
    print("e")

if not "abc":
    print("f")

if [1, 2, 3]:
    print("g")

if []:
    print("h")

if not []:
    print("i")

if not set():
    print("j")

if set():
    print("k")

if not {}:
    print("l")

if not tuple():
    print("m")

# Numbers evaluate to False if they are 0
if 1:
    print("n")

if 0:
    print("o")

if not 0.0:
    print("p")

# Objects return true by default
class MyClass:
    def __init__(self):
        return

my_object = MyClass()

if my_object:
    print("q")

# None is always False
if not None:
    print("r")


# --- Using "is" ---
# When checking if something is None, we usually use the following:
none_var = None
if none_var is None:
    print("s")

if none_var is not None:
    print("t")

# Reason (advanced): None is a singleton

