class IntervalTree(object):

  class Node(object):
    def __init__(self, low, high, maximum):
      self._low = low
      self._high = high
      self._maximum = maximum
      self._left = self._right = None

  def __init__(self):
    self._root = None

  def insert(self, low, high):
    if low > high:
      raise Exception("low greater than high")
    if not self._root:
      self._root = self.Node(low, high, high)
    else:
      self._insert(low, high, self._root)

  def _insert(self, low, high, cur):
    while True:
      cur._maximum = max(cur._maximum, high)
      if low < cur._low:
        if not cur._left:
          cur._left = self.Node(low, high, high)
          return
        else:
          cur = cur._left
      else:
        if not cur._right:
          cur._right = self.Node(low, high, high)
          return
        else:
          cur = cur._right

  def search(self, low, high):
    cur = self._root
    while True:
      if not cur:
        return None
      elif self._intersect(low, high, cur._low, cur._high):
        return cur._low, cur._high
      elif cur._left and cur._left._maximum >= low:
        cur = cur._left
      else:
        cur = cur._right

  def _intersect(self, l1, h1, l2, h2):
    if h1 < l2 or h2 < l1:
      return False
    return True      

  def __str__(self):
    return '\n'.join(self._print(self._root))

  def _print(self, cur):
    if not cur:
      return []
    else:
      result = []
      result.extend(['  ' + line for line in self._print(cur._left)])
      result.append('%d %d %d' % (cur._low, cur._high, cur._maximum))
      result.extend(['  ' + line for line in self._print(cur._right)])
      return result