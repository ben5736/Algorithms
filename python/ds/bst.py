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
    while True:
      if val < cur._val:
        if not cur._left:
          cur._left = self.Node(val)
          return
        else:
          cur = cur._left
      else:
        if not cur._right:
          cur._right = self.Node(val)
          return
        else:
          cur = cur._right

  def search(self, val):
    return self._search(val)[1] is not None

  def _search(self, val):
    parent = None
    cur = self._root
    while True:
      if not cur:
        return None, None
      elif cur._val == val:
        return parent, cur
      elif cur._val < val:
        parent = cur
        cur = cur._right
      else:
        parent = cur
        cur = cur._left

  def delete(self, val):
    parent, target = self._search(val)
    if not target:
      raise Exception("Element not in BST: " + val)
    if self._isLeaf(target):
        self._relink(parent, target, None)
    elif not target._left:
      self._relink(parent, target, target._right)
    elif not target._right:
      self._relink(parent, target, target._left)
    elif not target._left._right:
      target._left._right = target._right
      self._relink(parent, target, target._left)
    else:
      parent = target._left
      while parent._right._right:
        parent = parent._right
      target._val = parent._right._val  
      parent._right = None

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

  def __str__(self):
    return self._print(self._root)

  def _print(self, cur):
    if not cur:
      return ''
    else:
      return '[%s] %d [%s]' % (self._print(cur._left), cur._val, self._print(cur._right))