import sys

class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)

class ListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval
    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.getData()

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        
def parseExpressionToTree(expression):
    expressionList = expression.split()
    parentStack = ListStack()
    expressionTree = TreeNode(None)
    parentStack.push(expressionTree)
    currentTree = expressionTree
    
    for char in expressionList:
        if char == '(':
            currentTree.left = TreeNode('')
            parentStack.push(currentTree)
            currentTree = currentTree.left
        elif char in ['+', '-', '/', '*']:
            currentTree.data = char
            currentTree.right = TreeNode('')
            parentStack.push(currentTree)
            currentTree = currentTree.right
        elif char == ')':
            currentTree = parentStack.pop()
        elif char not in ['+', '-', '/', '*']:
            try:
                currentTree.data = int(char)
                currentTree = parentStack.pop()
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(char))
    
    return expressionTree
        
def evaluateExpressionTree(root):
    if root is not None:
        x = evaluateExpressionTree(root.left)
        y = evaluateExpressionTree(root.right)
        if (root.data == '+'):
            return x + y
        elif (root.data == '-'):
            return x - y
        elif (root.data == '/'):
            return x / y
        elif (root.data == '*'):
            return x * y
        else:
            return root.data
        
if __name__ == "__main__":
    tree = parseExpressionToTree(sys.argv[1])
    print(evaluateExpressionTree(tree))