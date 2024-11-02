# Import specific functions:
from my_area_functions import square_area, rectangle_area
print(square_area(10))
print(rectangle_area(5, 6))

# Import whole module:
import my_area_functions
print(my_area_functions.square_area(10))
print(my_area_functions.circle_area(4))
# Explain why we need to have module name first: because there might be name clashes

# Import while renaming module:
import my_area_functions as area
print(area.square_area(10))
print(area.circle_area(4))

# explain what import is doing (basically copy-pasting the whole file / specific function(s))
# explain why we want to write stuff in different files
# explain structure: we usually have import statements at the top of the file

# Explain: for now, we can consider all of these roughly equivalent:
# - Module
# - Package
# - Library
# - Framework
# The difference is that as you go down the list, they become "larger".
# Modules can be a single file, while a Library is often a collection of Modules,
# while a Framework has so much code that you just need to write a little bit (relatively)