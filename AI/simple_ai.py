# This is Artificial Intelligence but not Machine Learning
def chatbot(user_input):
    if user_input == "hello":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm just a simple AI, but I'm doing well!"
    elif user_input == "bye":
        return "Goodbye!"
    return "I don't understand."

print(chatbot("hello"))  # Output: Hi there!
print(chatbot("bye"))  # Output: Goodbye!