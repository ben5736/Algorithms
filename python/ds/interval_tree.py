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

  def _searchExact(self, low, high):
    path = []
    cur = self._root
    while cur and (cur._low != low or cur._high != high):
      path.append(cur)
      if low < cur._low:
        cur = cur._left
      else:
        cur = cur._right
    if cur:
      path.append(cur)
      return path
    return None

  def delete(self, low, high):
    path = self._searchExact(low, high)
    if not path:
      raise Exception("interval not found")
    if len(path) == 1:
      parent, target = None, path[-1]
    else:
      parent, target = path[-2], path[-1]

    if self._isLeaf(target):
      self._relink(parent, target, None)
      path.pop()
    elif not target._left:
      self._relink(parent, target, target._right)
      path.pop()
    elif not target._right:
      self._relink(parent, target, target._left)
      path.pop()
    elif not target._left._right:
      path[-1] = target._left
      target._left._right = target._right
      self._relink(parent, target, target._left)
    else:
      parent = target._left
      path.append(parent)
      while parent._right._right:
        parent = parent._right
        path.append(parent)
      target._low = parent._right._low  
      target._high = parent._right._high  
      parent._right = None

    for node in reversed(path):
      node._maximum = node._high
      if node._left and node._left._maximum > node._maximum:
        node._maximum = node._left._maximum
      if node._right and node._right._maximum > node._maximum:
        node._maximum = node._right._maximum

  def _relink(self, parent, target, new_target):
    if not parent:
      self._root = new_target
    elif target == parent._left:
      parent._left = new_target
    elif target == parent._right:
      parent._right = new_target
    else:
      raise Exception("Cannot unlink when target is not a child of parent.")

  def _isLeaf(self, node):
    return not node._left and not node._right

  def _intersect(self, l1, h1, l2, h2):
    if h1 < l2 or h2 < l1:
      return False
    return True      

  def __str__(self):
    return '\n' + '\n'.join(self._print(self._root)) + '\n'

  def _print(self, cur):
    if not cur:
      return []
    else:
      result = []
      result.extend(['  ' + line for line in self._print(cur._left)])
      result.append('%d %d %d' % (cur._low, cur._high, cur._maximum))
      result.extend(['  ' + line for line in self._print(cur._right)])
      return result