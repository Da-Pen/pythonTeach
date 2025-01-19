class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.length == 0:
            self.head = new_node
        self.length += 1

    def appendleft(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def __str__(self):
        if self.length == 0:
            return "[Empty DoublyLinkedList]"
        s = "None <- "
        cur_node = self.head
        while cur_node:
            s += str(cur_node.data)
            if cur_node.next:
                s += " <-> "
            cur_node = cur_node.next
        s += " -> None"
        return s

    def __len__(self):
        return self.length

    def extend(self, l):
        for x in l:
            self.append(x)

    def extendleft(self, l):
        for x in l:
            self.appendleft(x)

    def pop(self):
        if self.length == 0:
            raise IndexError("Cannot pop on empty LinkedList")

        data = self.tail.data

        if self.length == 1:
            self.clear()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        return data

    def popleft(self):
        if self.length == 0:
            raise IndexError("Cannot popleft on empty LinkedList")

        data = self.head.data

        if self.length == 1:
            self.clear()
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

        return data

    def insert(self, i, x):
        if  i < 0 or self.length < i:
            raise IndexError(f"LinkedList index out of range: {i}")

        # special cases: insert at beginning or end
        if i == 0:
            self.appendleft(x)
            return

        if i == self.length:
            self.append(x)
            return

        # "normal" case: insert new node between two existing nodes
        # go to node at index i-1 (it will be the node before the new node)
        cur_index = 0
        cur_node = self.head
        while cur_index < i - 1:
            cur_node = cur_node.next
            cur_index += 1

        # create new node and link it to previous and next nodes
        new_node = Node(x)
        new_node.prev = cur_node
        new_node.next = cur_node.next

        # link previous and next nodes to new node
        cur_node.next.prev = new_node
        cur_node.next = new_node

        self.length += 1

# Example usage
dll = DoublyLinkedList()
print(dll)
print(len(dll))
dll.extendleft([3, 2, 1])
dll.extend([4, 5, 6])
dll.append(7)
dll.appendleft(0)
print(dll)
print(dll.pop())
print(dll.popleft())
dll.clear()
print(dll)
print(len(dll))
# dll.pop()
dll.insert(0, 2)
dll.insert(0, 1)
dll.insert(2, 4)
dll.insert(2, 3)
print(dll)
