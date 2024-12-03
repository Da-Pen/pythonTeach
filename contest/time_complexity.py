# When we write code, we want to make it as efficient as possible.
# However, since computers are so fast, it will only make a difference
# when inputs are EXTREMELY large.

# So, we measure something called TIME COMPLEXITY, which is a way of analyzing
# how the runtime of an algorithm changes as the input size increases.

# Example: Constant Time Complexity
def get_first_item(my_list):
    return my_list[0]

# Note that the speed of this function doesn't depend on the size of my_list.
# If my list has 1 item or 100 items or 10000000 items, it will be roughly the same fast.
# We say that this has CONSTANT TIME COMPLEXITY, or that it is O(1)

# ---
# Example: Linear Time Complexity
def print_all_items(my_list):
    for item in my_list:
        print(item)

# If my_list doubles in size, what happens to the runtime of this function?
# It would also double (approximately). If my_list is 100x the size of before, it would
# take 100x as much time to run.
# We say this has LINEAR TIME COMPLEXITY, or that it is O(n)


# ---
# Example: Quadratic Time Complexity
def print_multiplication_table(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i] * my_list[j], end="\t")
        print()  # print newline

print_multiplication_table([1, 2, 3, 4])

# If my_list doubles in size, the runtime of this function would approximately 4x.
# If my_list triples in size, the runtime of this function would approximately 9x.
# If my_list quadruples in size, the runtime of this function would approximately 16x.
# We say this has a runtime of O(n^2)

# Example of O(log(n)) runtime: binary search.
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

# Notice that each run of binary search, ignoring recursive calls, is constant time.
# Now let's consider how many times we will make recursive calls.
# Examples:
#   my_list = [1, 2] -> max. 2 runs of function
#   my_list = [1, 2, 3, 4] -> max. 3 runs of function
#   my_list = [1, 2, 3, 4, 5, 6, 7, 8] -> max. 4 runs of function
#   my_list = [1, ..., 16] -> max. 8 runs of function

# We see that the patterns is # runs of function ~= log(len(my_list))
# Therefore the runtime is O(log(n)).

# Exercises: What are the time complexities of the following functions?
def func_1(my_list):
    if len(my_list) == 0:
        return None
    return my_list[0] + my_list[-1]

def func_2(my_list):
    product = 1
    for num in my_list:
        product *= num
    return product

def func_3(my_list):
    for i in range(0, len(list), 3):
        print(my_list[i])

def func_4(my_dictionary):
    return my_dictionary.get("key")

def func_5(my_dictionary):
    for key in my_dictionary:
        print(my_dictionary[key])

def func_6(my_list):
    if len(my_list) < 1000:
        return
    for i in range(1000):
        print(my_list[i])

def func_7(my_list):
    for i in range(0, len(list), 3):
        print(my_list[i])
    for i in range(1, len(list), 3):
        print(my_list[i])
    for i in range(2, len(list), 3):
        print(my_list[i])

def func_8(my_list):
    i = len(list) - 1
    while i > 1:
        print(my_list[i])
        i = i // 2

def func_9(my_set):
    sum = 0
    for item in my_set:
        sum += item
    return sum

def func_10(my_list):
    return [n + 5 for n in my_list]

def func_11(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                print(my_list[i], my_list[j], my_list[k])

def func_12(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(1000):
                print(my_list[i], my_list[j])

def func_13(my_list):
    i = 1
    while i < len(my_list):
        print(my_list[i])
        i *= 2

def func_14(my_list):
    i = 1
    while i < len(my_list):
        print(my_list[i])
        i *= 5

def func_15(my_list):
    i = 1
    while i < len(my_list):
        if my_list[i] == 12345:
            return
        i *= 2

def func_16(my_list):
    i = 0
    while i < len(my_list):
        for num in my_list:
            print(num)
        i += 10
