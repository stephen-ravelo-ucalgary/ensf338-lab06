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

# Array Binary Search
def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Create BST using shuffled vector
shuffled_vector = list(range(1, 10001))
random.shuffle(shuffled_vector)

r = Node(1)
for i in shuffled_vector:
    r = insert(r, i)

# Timing BST Search using shuffled vector
bst_avg_time = 0
bst_total_time = 0

for i in range(1, 10001):
    elapsed_time = timeit.timeit(lambda : search(r, i), number = 10)
    bst_total_time += (elapsed_time / 10)

bst_avg_time = bst_total_time / 10000

print("Binary Search Tree Performance using Shuffled Vector")
print("Average Time:", bst_avg_time, "seconds")
print("Total Time:", bst_total_time, "seconds")

# Create sorted array
sorted_vector = list(range(1, 10001))

# Timing binary search on arrays
bin_search_avg_time = 0
bin_search_total_time = 0

for i in range(1, 10001):
    elapsed_time = timeit.timeit(lambda : binarySearch(sorted_vector, 0, 9999, i), number = 10)
    bin_search_total_time += (elapsed_time / 10)

bin_search_avg_time = bin_search_total_time / 10000

print("\nArray Binary Search Performance")
print("Average Time:", bin_search_avg_time, "seconds")
print("Total Time:", bin_search_total_time, "seconds")

'''
Question 4 Answer
Searching for an element in a binary search tree is slightly faster than binary search on an array. The
difference is about 0.005 seconds. Although, both of these algorithms have the same complexity of O(log n).
The difference is possibly a result of the way the two search algorithms are implemented. Binary search on
an array is done iteratively, while search on a binary search tree is recursive. The operations involved
in the iterative solution are possibly more time consuming than the operations involved in the recursive
solution.
'''
