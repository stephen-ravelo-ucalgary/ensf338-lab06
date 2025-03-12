class Heap:
    def __init__(self):
        self.heap = []
        
    def heapify(self, arr):
        # Receives an input of an array of integers, stores it into an array and turn it into a heap.
        self.heap = arr[:]
        
        
    def heapifyDown(self, index):
        size = len(self.heap)
        rightIndex = index * 2 + 2
        if((rightIndex < size) and (self.heap[index] < self.heap[rightIndex])):
            self.heap[index], self.heap[rightIndex] = self.heap[rightIndex], self.heap[index]
        self.heapifyDown(rightIndex)
    
    def heapifyUp(self, index):
        parentIndex = (index - 1) // 2
        
        if((parentIndex >= 0) and (self.heap[index] > self.heap[parentIndex])):
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
        
        self.heapifyUp(parentIndex)
        
    
    def enqueue(self, value):
        self.heap.append(value)
        lastIndex = len(self.heap) - 1
        self.heapifyUp(lastIndex)
    
    def dequeue(self):
        lastIndex = len(self.heap) - 1
        self.heap[0] = self.heap[lastIndex]
        self.heap.pop(lastIndex)
        self.heapifyDown(0)
    
class Tester:
    # Write 3 tests for following cases:
        # Input array is already a correctly sorted heap.
        # Input array is empty.
        # Input array is a long, randomly shuffled list of integers.
        