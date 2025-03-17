import random
import timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        newNode = Node(value)
        
        if((self.head is None) or (value < self.head.value)):
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            
            while((current.next is not None) and (current.next.value <= value)):
                current = current.next
            
            newNode.next = current.next
            current.next = newNode
    
    def dequeue(self):
        if(self.head is None):
            return None

        value = self.head.value
        self.head = self.head.next
        return value

class HeapPriorityQueue:
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


        
def generateTasks():
    numTasks = 1000
    enqueueProb = 0.7
    tasks = []
    for _ in range(numTasks):
        if (random.random() < enqueueProb):
            tasks.append(("enqueue", random.randint(1, 10000)))
        else:
            tasks.append(("dequeue", None))
    return tasks

def processTasks(tasks, arr):
    for task, value in tasks:
        if(task == "enqueue"):
            arr.enqueue(value)
        elif(task == "dequeue"):
            arr.dequeue()
    
    return arr

def runTasks(arrClass, tasks):
    arr = arrClass()
    processTasks(tasks, arr)
    
def measureTime(arrClass, tasks):
    number = 1;
    totalTime = timeit.timeit(lambda: runTasks(arrClass, tasks), number=number)
    avgTime = totalTime / len(tasks)
    
    return totalTime, avgTime

if __name__ == "__main__":
    tasks = generateTasks()
    
    pqTotal, pqAverage = measureTime(ListPriorityQueue, tasks)
    print("ListPriorityQueue Total Time: {}s".format(pqTotal))
    print("ListPriorityQueue Average Time: {}s".format(pqAverage))
    
    heapTotal, heapAverage = measureTime(HeapPriorityQueue, tasks)
    print("HeapPriorityQueue Total Time: {}s".format(heapTotal))
    print("HeapPriorityQueue Average Time: {}s".format(heapAverage))



# Question 4:
#   The timing results show that the HeapPriorityQueue is faster than the ListPriorityQueue when processing
#   a sequence of 1000 generated tasks. This is due to the linked list's enqueue operation requiring traversing the
#   list to maintain order, where the action of traversing a list has a worst case complexity of O(n). The
#   heap based appreoach uses heapifyDown and heapifyUp which is O(log n). This demonstrates that as the
#   number of tasks increase, the more efficient the HeapPriorityQueue will be compared to the ListPriorityQueue.