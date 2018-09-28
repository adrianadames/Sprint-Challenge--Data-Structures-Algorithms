def heapsort(arr):
  heap = Heap()
  sorted = []
  for i in arr:
    heap.insert(i)
  while len(heap.storage)>0:
    sorted.append(heap.delete())
  sorted.reverse()
  return sorted

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2


# ### DEMO ###

# #random assortment of the integers 1-100
# arr1 = [24, 87, 86, 50, 32, 67, 28, 13, 14, 51, 41, 18, 47, 90, 33, 5, 59, 11, 54, 31, 58, 100, 22, 8, 88, 85, 96, 53, 35, 57, 74, 98, 81, 6, 65, 9, 70, 23, 26, 30, 25, 34, 45, 15, 2, 83, 69, 20, 44, 10, 72, 73, 21, 39, 92, 99, 38, 55, 78, 46, 63, 4, 95, 71, 61, 42, 12, 1, 82, 89, 17, 77, 29, 16, 60, 40, 56, 62, 91, 48, 64, 19, 36, 97, 7, 94, 3, 49, 93, 84, 80, 27, 79, 66, 52, 37, 75, 76, 43, 68]
# # arr2 = [14, 48, 73, 26, 34, 30, 60, 96, 100, 55, 4, 27, 19, 66, 76, 28, 80, 9, 99, 41, 65, 31, 7, 23, 92, 42, 35, 36, 37, 1, 11, 20, 81, 58, 44, 15, 22, 61, 94, 71, 25, 21, 24, 57, 12, 64, 89, 78, 63, 83, 29, 46, 91, 62, 47, 45, 86, 93, 38, 5, 51, 69, 74, 49, 39, 87, 88, 3, 16, 95, 18, 75, 97, 79, 77, 53, 56, 17, 98, 85, 68, 70, 72, 10, 6, 50, 67, 54, 8, 2, 40, 32, 90, 33, 43, 13, 52, 59, 84, 82]
# # for i in arr2:
#   # arr1.append(i)
# print(heapsort(arr1))