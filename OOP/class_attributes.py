class User:
    next_id = 1  # Shared counter for unique user IDs

    def __init__(self, name):
        self.name = name
        self.id = User.next_id
        User.next_id += 1

user1 = User("Alice")
user2 = User("Bob")
print(user1.id)  # Output: 1
print(user2.id)  # Output: 2
