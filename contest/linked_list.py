# # Explain that we can use objects to create our own "data types"

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # Note: methods are in order of implementation for learners
    def __init__(self):
        self.head = None

    def appendleft(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def clear(self):
        self.head = None

    def __str__(self):
        if len(self) == 0:
            return "[Empty LinkedList]"
        cur_node = self.head
        s = ""
        while cur_node:
            s += str(cur_node.data) + " -> "
            cur_node = cur_node.next
        s += "None"
        return s

    def append(self, data):
        new_node = Node(data)

        # special case: if LinkedList is empty, just set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # go to last node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node

    def __len__(self):
        len = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            len += 1
        return len

    def extend(self, l):
        for x in l:
            self.append(x)

    def extendleft(self, l):
        for x in l:
            self.appendleft(x)

    def popleft(self):
        # special case: list is empty
        if not self.head:
            raise IndexError("Cannot popleft on empty LinkedList")

        data = self.head.data
        self.head = self.head.next
        return data

    def pop(self):
        # special case: list is empty
        if not self.head:
            raise IndexError("Cannot pop on empty LinkedList")

        # special case: one item in list
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        cur_node = self.head
        while cur_node.next.next:
            cur_node = cur_node.next

        data = cur_node.next.data
        cur_node.next = None
        return data

    def insert(self, i, x):
        # special case: insert at index 0
        if i == 0:
            self.appendleft(x)
            return

        new_node = Node(x)

        # go to node at index i-1
        cur_i = 0
        cur_node = self.head

        while cur_i < i - 1:
            cur_node = cur_node.next
            cur_i += 1
            if not cur_node:
                raise IndexError(f"LinkedList index out of range: {i}")

        new_node.next = cur_node.next
        cur_node.next = new_node


ll = LinkedList()
ll.extend([1, 2, 3])
print(ll)
ll.insert(3, 4)
ll.appendleft(0)
print(ll)
print(len(ll))
ll.pop()
print(ll)
ll.popleft()
print(ll)
ll.clear()
print(ll)
# ll.pop()



# Improvements
# - keep track of length
# - keep track of beginning and end
