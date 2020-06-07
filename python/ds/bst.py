class BST(object):

  class Node(object):
    def __init__(self, val):
      self._val = val
      self._left = self._right = None

  def __init__(self):
    self._root = None

  def insert(self, val):
    if not self._root:
      self._root = self.Node(val)
    else:
      self._insert(val, self._root)

  def _insert(self, val, cur):
    if val < cur._val:
      if not cur._left:
        cur._left = self.Node(val)
      else:
        self._insert(val, cur._left)
    else:
      if not cur._right:
        cur._right = self.Node(val)
      else:
        self._insert(val, cur._right)

  def search(self, val):
    cur = self._root
    while True:
      if not cur:
        return False
      elif cur._val == val:
        return True
      elif cur._val < val:
        cur = cur._right
      else:
        cur = cur._left

  def __str__(self):
    return self._print(self._root)

  def _print(self, cur):
    if not cur:
      return ''
    else:
      return '[%s] %d [%s]' % (self._print(cur._left), cur._val, self._print(cur._right))