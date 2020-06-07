import unittest

import interval_tree

class IntervalTreeTest(unittest.TestCase):

  def testEmpty(self):
    t = interval_tree.IntervalTree()
    self.assertEqual(t.search(3, 5), None)
    self.assertEqual(str(t), '')

  def testOne(self):
    t = interval_tree.IntervalTree()
    t.insert(2, 4)
    self.assertEqual(t.search(3, 5), (2, 4))
    self.assertEqual(str(t), '2 4 4')

  def testTwo(self):
    t = interval_tree.IntervalTree()
    t.insert(2, 4)
    t.insert(3, 6)
    self.assertEqual(t.search(3, 4), (2, 4))
    self.assertEqual(t.search(5, 6), (3, 6))
    self.assertEqual(str(t),
"""2 4 6
  3 6 6""")

  def testThree(self):
    t = interval_tree.IntervalTree()
    t.insert(4, 6)
    t.insert(3, 8)
    t.insert(6, 7)
    self.assertEqual(t.search(3, 4), (4, 6))
    self.assertEqual(t.search(7, 7), (3, 8))
    self.assertEqual(str(t),
"""  3 8 8
4 6 8
  6 7 7""")


if __name__ == '__main__':
  unittest.main()