# Tuples are just like lists, except you can't edit them.
# You can't update values, add items, or remove items.

my_tuple = ("this", "is", "a", "tuple")
print(len(my_tuple))
print(my_tuple[1])

# Doesn't work!
# my_tuple.append("CANNOT APPEND TO A TUPLE!")
# my_tuple[1] = "CAN'T UPDATE A TUPLE ITEM EITHER!"

for word in my_tuple:
    print(word)

print("this" in my_tuple)

empty_tuple = ()

tuple_with_one_item_WRONG = (54)
print(tuple_with_one_item_WRONG)

tuple_with_one_item = (54,)
print(tuple_with_one_item)

# explain briefly why we sometimes use a tuple over a list:
#   - prevent accidental changes (other people work on code and might change a list even though you don't want it)
#   - more efficient
#   - hashable (for now, just explain that they can be used in keys of dictionaries, will explain later why)

