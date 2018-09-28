# Stack's alternative name is LIFO (last in, first out)
class Stack:
    def __init__(self):
      self.items = []
    
    def push(self,item):
      self.items.append(item)

    def pop(self):
      return self.items.pop()

# Queue's alternative name is FIFO (first in, first out)
class Queue:
  def __init__(self):
    self.items = []
  
  #Insert item to end of queue
  def enqueue(self, item):
    self.items.append(item)

  #Delete first item in the queue
  def dequeue(self):
    return self.items.pop(0)

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    dfsContainer = []
    stack = Stack()
    currentNode = self
    finished = False

    while finished is False:
      if currentNode is not None:
        stack.push(currentNode)
        currentNode = currentNode.left
      else:
        if len(stack.items)>0:
          currentNode = stack.pop()
          dfsContainer.append(currentNode.value)
          currentNode = currentNode.right
        else:
          finished = True
    return dfsContainer

  def breadth_first_for_each(self, cb):
    bfsContainer = []
    queue = Queue()
    currentNode = self
    finished = False
    traversed = []
    
    if currentNode:
      queue.enqueue(currentNode)
    while len(queue.items)>0:
      currentNode = queue.dequeue()
      if currentNode not in traversed:
        traversed.append(currentNode)
        bfsContainer.append(currentNode.value)
        if currentNode.left:
          queue.enqueue(currentNode.left)
        if currentNode.right:
          queue.enqueue(currentNode.right)
    return bfsContainer

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

bst1 = BinarySearchTree(8)
bst1.insert(3)
bst1.insert(1)
bst1.insert(6)
bst1.insert(4)
bst1.insert(7)
bst1.insert(10)
bst1.insert(14)
bst1.insert(13)

# print(bst1.depth_first_for_each(lambda x:x))
print(bst1.breadth_first_for_each(lambda x:x))