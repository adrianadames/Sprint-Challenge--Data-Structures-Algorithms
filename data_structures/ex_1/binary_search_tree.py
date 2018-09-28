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
    print(dfsContainer)

  def breadth_first_for_each(self, cb):
    bfsContainer = []
    queue = Queue()
    currentNode = self
    finished = False
    traversed = []

    while finished is False:
      if currentNode is not None:
        queue.enqueue(currentNode)
        # bfsContainer.append(currentNode.value)
        if currentNode.left:
          queue.enqueue(currentNode.left)
        if currentNode.right:
          queue.enqueue(currentNode.right)
        traversed.append(currentNode)
        removed = queue.dequeue()
        if removed is not in traversed:
          currentNode = currentNode.
        else:
          finished = True

        


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



# stack1 = Stack()
# stack1.push(4)
# stack1.push(5)
# stack1.push(6)
# print(stack1.items)
# print(stack1.pop())
# print(stack1.items)

# q1 = Queue()
# q1.enqueue(4)
# q1.enqueue(5)
# q1.enqueue(6)
# q1.enqueue(7)
# print(q1.items)
# q1.dequeue()
# print(q1.items)


bst1 = BinarySearchTree(8)
bst1.insert(3)
bst1.insert(1)
# bst1.insert(6)
# bst1.insert(4)
# bst1.insert(7)
bst1.insert(10)
bst1.insert(14)
# bst1.insert(13)

# print(bst1.value)
# print(bst1.left.value)
# print(bst1.left.left.value)
# print(bst1.right.value)
# print(bst1.right.right.value)
# print(bst1.value)

# bst1.depth_first_for_each(lambda x:x)
bst1.breadth_first_for_each(lambda x:x)