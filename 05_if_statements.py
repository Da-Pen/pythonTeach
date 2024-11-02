# Example 1
money = 1.25
bags_of_chips_cost = 1.50

if money >= bags_of_chips_cost:
    print("You have enough money to buy a bag of chips!")
else:
    print("You don't have enough money to buy a bag of chips :(")


# Example 2
age = 12
drunk = False
if age >= 16 and not drunk:
    print("You can drive")
elif age >= 16:
    print("You can't drive because you're drunk")
elif not drunk:
    print("You can't drive because you're too young")
else:
    print("You can't drive because you're too young and you're drunk")

# Exercise: write a program that prints "even" if a number is even, and "odd" if it's odd
# Exercise: now make it accept fractions. If it's not a whole number, print "it's a fraction"
