import timeit
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

# Create BST using sorted vector
r = Node(1)
for i in range(2, 10001):
    r = insert(r, i)

# Timing BST Search using sorted vector
sorted_avg_time = 0
sorted_total_time = 0

for i in range(1, 10001):
    elapsed_time = timeit.timeit(lambda : search(r, i), number = 10)
    sorted_total_time += (elapsed_time / 10)

sorted_avg_time = sorted_total_time / 10000

print("Binary Search Tree Performance using Sorted Vector")
print("Average Time: ", sorted_avg_time, "seconds")
print("Total Time: ", sorted_total_time, "seconds")

# Create BST using shuffled vector
vector = list(range(1, 10001))
random.shuffle(vector)

newR = Node(1)
for i in vector:
    newR = insert(newR, i)

# Timing BST Search using shuffled vector
shuffled_avg_time = 0
shuffled_total_time = 0

for i in range(1, 10001):
    elapsed_time = timeit.timeit(lambda : search(newR, i), number = 10)
    shuffled_total_time += (elapsed_time / 10)

shuffled_avg_time = shuffled_total_time / 10000

print("\nBinary Search Tree Performance using Shuffled Vector")
print("Average Time: ", shuffled_avg_time, "seconds")
print("Total Time: ", shuffled_total_time, "seconds")

'''
Question 4 Answer
Searching a BST that is built using a shuffled vector is significantly faster than if it is built using
a sorted vector.
Using the sorted vector creates an extremely unbalanced tree where all succeeding elements are placed to the
right of each node, resulting in a tree similar to a linked list. Searching for an element has a complexity of O(n).
Using the shuffled vector creates a more balanced BST due to its randomness. Some elements end up on the
left and some on the right. This results in a smaller tree height closer to O(log n), which is also its
search time complexity.
'''
