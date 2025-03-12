import random
import sys
sys.setrecursionlimit(11000)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# BST Insertion
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

# BST Search
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

# Following four functions are for balancing a binary search tree
def storeInorder(root, nodes):
    if root is None:
        return

    # Traverse the left subtree
    storeInorder(root.left, nodes)

    # Store the node data
    nodes.append(root.val)

    # Traverse the right subtree
    storeInorder(root.right, nodes)

# Function to build a balanced BST from a sorted array
def buildBalancedTree(nodes, start, end):
    # Base case
    if start > end:
        return None

    # Get the middle element and make it the root
    mid = (start + end) // 2
    root = Node(nodes[mid])

    # Recursively build the left and right subtrees
    root.left = buildBalancedTree(nodes, start, mid - 1)
    root.right = buildBalancedTree(nodes, mid + 1, end)

    return root

# Function to balance a BST
def balanceBST(root):
    nodes = []

    # Store the nodes in sorted order
    storeInorder(root, nodes)

    # Build the balanced tree from the sorted nodes
    return buildBalancedTree(nodes, 0, len(nodes) - 1)

# Print tree as level order
from collections import deque

def printLevelOrder(root):
    if root is None:
        print("N", end=" ")
        return

    queue = deque([root])
    nonNull = 1

    while queue and nonNull > 0:
        curr = queue.popleft()

        if curr is None:
            print("N", end=" ")
            continue
        nonNull -= 1

        print(curr.val, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
        if curr.left:
            nonNull += 1
        if curr.right:
            nonNull += 1


r = Node(1)
for i in range(2, 21):
    r = insert(r, i)



balancedRoot = balanceBST(r)
printLevelOrder(balancedRoot)

print("Found" if search(balancedRoot, 19) else "Not Found")
print("Found" if search(balancedRoot, 20) else "Not Found")

newR = Node(1)
x_list = list(range(2, 21))
print(x_list)
random.shuffle(x_list)
print(x_list)
for i in x_list:
    newR = insert(newR, i)

balancedRoot = balanceBST(newR)
printLevelOrder(balancedRoot)