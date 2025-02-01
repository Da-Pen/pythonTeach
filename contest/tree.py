from collections import deque

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def depth_first_search(root, value):
    if not root:
        return False
    if root.value == value:
        return True
    return depth_first_search(root.left, value) or depth_first_search(root.right, value)


def breadth_first_search(root, value):
    queue = deque([root])
    while queue:
        cur_node = queue.popleft()
        if not cur_node:
            continue
        if cur_node.value == value:
            return True
        queue.append(cur_node.left)
        queue.append(cur_node.right)
    return False


 #      1
 #    /   \
 #   2     3
 #  /     / \
 # 4     5   6

node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6

print(depth_first_search(node1, 6))
print(breadth_first_search(node1, 6))

# Exercise: implement a non-binary tree with DFS and BFS
# Exercise: get height of a tree
def height_helper(root, cur_height):
    if not root:
        return 0
    return 1 + max(
        height_helper(root.left, cur_height),
        height_helper(root.right, cur_height))

def height(root):
    return height_helper(root, 0)

print(height(node1))

# Exercise: write a function that takes two trees and returns True if
# they are identical (same structure and values)

# Exercise: given a BST and a target, return True if the target is in the BST and false otherwise

# Exercise: write a function that takes a binary tree and determines if it's a BST
