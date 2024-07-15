import bisect

# class SnapshotSet(object):

#   def __init__(self):
#     self.main = set()
#     self.added = set()
#     self.removed = set()
#     self.pending_iter = False

#   def add(self, value):
#     if not self.pending_iter:
#       return self.main.add(value)
#     elif self.pending_iter.has_next():
#       self.added.add(value)
#       self.removed.remove(value)
#     else:
#       self.merge()
#       self.main.add(value)

#   def remove(self, value):
#     if not self.pending_iter:
#       return self.main.remove(value)
#     elif self.pending_iter.has_next():
#       self.added.remove(value)
#       self.removed.added(value)
#     else:
#       self.merge()
#       self.main.remove(value)

#   def contains(self, value):
#     if not self.pending_iter:
#       return self.main.contains(value)
#     elif self.pending_iter.has_next():
#       return self.added.contains(value) or (self.main.contains(value) and not self.removed.contains(value))
#     else:
#       self.merge()
#       return self.main.contains(value)

#   def iterator(self):
#     self.merge()
#     self.pending_iter = iter(self.main)
#     return self.pending_iter

#   def merge():
#     for v in self.added:
#       self.main.add(v)
#     for v in self.removed:
#       self.main.remove(v)

from collections import defaultdict

class NewSnapshotSet(object):

  def __init__(self):
    self.snapshot = 0
    self.inner_set = defaultdict(list)
    self.array = []

  def add(self, value):
    changes = self.inner_set[value]
    if len(changes) == 0:
      changes.append((self.snapshot, True))
      self.array.append((value, changes))
    elif not changes[-1][1]:
      if self.snapshot == changes[-1][0]:
        changes.pop()
      else:
        changes.append((self.snapshot, True))

  def remove(self, value):
    if not self.contains(value):
      raise Exception("non existing value")
    changes = self.inner_set[value]
    if self.snapshot == changes[-1][0]:
      changes.pop()
    else:
      changes.append((self.snapshot, False))

  def contains(self, value):
    if value not in self.inner_set:
      return False

    changes = self.inner_set[value]
    if len(changes) == 0:
      return False

    return changes[-1][1] 

  def iterator(self):
    ret = self._Iterator(self, self.snapshot, len(self.array))
    self.snapshot += 1
    return ret

  class _Iterator(object):

    def __init__(self, container, snapshot, array_length):
      self.container = container
      self.snapshot = snapshot
      self.array_length = array_length
      self.next_pos = 0

    def __iter__(self):
      return self

    def next(self):
      return self.__next__()

    def __next__(self):
      while self.next_pos < self.array_length:
        value, changes = self.container.array[self.next_pos]
        last_snapshot_index = bisect.bisect_right(changes, (self.snapshot, True))
        if last_snapshot_index > 0:
          snapshot, change = changes[last_snapshot_index - 1]
          if change:
            self.next_pos += 1
            return value
        # for i in range(len(changes) - 1, -1, -1):
        #   snapshot, change = changes[i]
        #   if snapshot <= self.snapshot:
        #     if change:
        #       self.next_pos += 1
        #       return value
        #     else:
        #       break
        self.next_pos += 1
      raise StopIteration


import unittest

class Test(unittest.TestCase):

  def test1(self):
    s = NewSnapshotSet()
    s.add(1)

    self.assertTrue(s.contains(1))
    self.assertFalse(s.contains(2))

    s.add(2)
    self.assertTrue(s.contains(2))

    s.remove(1)
    self.assertFalse(s.contains(1))
    self.assertTrue(s.contains(2))

  def test2(self):
    s = NewSnapshotSet()
    s.add(1)
    s.add(2)
    s.add(3)

    iterator = s.iterator()
    s.add(4)
    s.remove(2)
    iterator2 = s.iterator()

    s.remove(1)
    s.remove(3)
    iter3 = s.iterator()

    s.add(1)
    s.add(2)
    iter4 = s.iterator()
    self.assertIterator(iterator, {1, 2, 3})
    self.assertIterator(iterator2, {1, 4, 3})
    self.assertIterator(iter3, {4})
    self.assertIterator(iter4, {1, 4, 2})

  def assertIterator(self, iterator, content):
    ns = set()
    for _ in range(len(content)):
      e = next(iterator)
      ns.add(e)
    self.assertEqual(ns, content)
    with self.assertRaises(StopIteration):
      next(iterator)

if __name__ == '__main__':
    unittest.main()