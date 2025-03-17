import random

class Heap:
    def __init__(self):
        self.heap = []
        
    def heapify(self, arr):
        # Receives an input of an array of integers, stores it into an array and turn it into a heap.
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(((n - 2) // 2), -1, -1):
            self.heapifyDown(i)
        
        
    def heapifyDown(self, index):
        size = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = index * 2 + 2
        
        if((left < size) and (self.heap[left] > self.heap[largest])):
            largest = left

        if((right < size) and (self.heap[right] > self.heap[largest])):
            largest = right
            
        if(largest != index):
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapifyDown(largest)
            
    def heapifyUp(self, index):
        if(index == 0):
            return

        parentIndex = (index - 1) // 2
        
        if(self.heap[index] > self.heap[parentIndex]):
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            self.heapifyUp(parentIndex)
        
    
    def enqueue(self, value):
        self.heap.append(value)
        lastIndex = len(self.heap) - 1
        self.heapifyUp(lastIndex)
    
    def dequeue(self):
        if(not self.heap):
            return None
        
        root = self.heap[0]
        lastIndex = len(self.heap) - 1
        
        self.heap[0] = self.heap[lastIndex]
        self.heap.pop()
        
        if(self.heap):
            self.heapifyDown(0)
        
        return root
    
class Tester:
    def testSortedHeap(self):
        arr = [20, 18, 15, 10, 12, 13]
        heap = Heap()
        heap.heapify(arr)
        
        if(heap.heap == arr):
            print("Test sorted heap: Pass")
        else:
            print("Test sorted heap: Fail")
            print("Expected: ", arr)
            print("Got: ", heap.heap)
    
    def testEmptyArray(self):
        arr = []
        heap = Heap()
        heap.heapify(arr)
        
        if(heap.heap == []):
            print("Test empty array: Pass")
        else:
            print("Test empty array: Fail")
            print("Expected: []")
            print("Got: ", heap.heap)
            
    def testRandomArray(self):
        arr = list(range(1, 101))
        random.shuffle(arr)
        heap = Heap()
        heap.heapify(arr)
        
        n = len(heap.heap)
        isHeap = True
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if((left < n) and (heap.heap[i] < heap.heap[left])):
                isHeap = False
                break
            
            if((right < n) and (heap.heap[i] < heap.heap[right])):
                isHeap = False
                break
            
        if(isHeap):
            print("Test random array: Pass")
        else:
            print("Test random array: Fail")
            print("Heap array: ", heap.heap)
        
    def runTests(self):
        self.testSortedHeap()
        self.testEmptyArray()
        self.testRandomArray()
        

if __name__ == "__main__":
    tester = Tester()
    tester.runTests()