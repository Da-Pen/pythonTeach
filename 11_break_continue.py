
# break
# Example: look for the first occurrence of 0 in a list of numbers
# numbers = [5, 2, 3, 0, 7, 9, 0, 3]
# for i in range(len(numbers)):
#     print(numbers[i])
#     if numbers[i] == 0:
#         print("The first occurrence of 0, is at index", i)
#         break

# Example: print messages from the user until they type "stop"
# while True:
#     message = input('Type a message (or "stop" to exit): ')
#     if message == "stop":
#         break
#     print("Your message was:", message)

# continue
# Task: A list has numbers mixed in with None's. Get the sum of all the numbers.
# ex. [3, 5, -4, None, 2, -1, None] => 5
nums = [3, 5, -4, None, 2, -1, None]
sum = 0
for num in nums:
    if num is None:
        continue
    print("Adding", num, "...")
    sum += num


print(sum)