# Stack's alternative name is LIFO (last in, first out)
class Stack:
    def __init__(self):
      self.items = []
    
    def push(self,item):
      self.items.append(item)

    def pop(self):
      return self.items.pop()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self):
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
    pass

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

bst1.depth_first_for_each()