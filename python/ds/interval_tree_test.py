import unittest

import interval_tree

class IntervalTreeTest(unittest.TestCase):
  
  def testInvalidInterval(self):
    t = interval_tree.IntervalTree()
    self.assertRaises(Exception, lambda:t.insert(5, 3))

  def testEmpty(self):
    t = interval_tree.IntervalTree()
    self.assertEqual(t.search(3, 5), None)
    self.assertEqual(str(t), 
"""

""")

  def testOne(self):
    t = interval_tree.IntervalTree()
    t.insert(2, 4)
    self.assertEqual(t.search(3, 5), (2, 4))
    self.assertEqual(str(t), 
"""
2 4 4
""")

  def testTwo(self):
    t = interval_tree.IntervalTree()
    t.insert(2, 4)
    t.insert(3, 6)
    self.assertEqual(t.search(3, 4), (2, 4))
    self.assertEqual(t.search(5, 6), (3, 6))
    self.assertEqual(str(t),
"""
2 4 6
  3 6 6
""")

  def testThree(self):
    t = interval_tree.IntervalTree()
    t.insert(4, 6)
    t.insert(3, 8)
    t.insert(6, 7)
    self.assertEqual(t.search(3, 4), (4, 6))
    self.assertEqual(t.search(7, 7), (3, 8))
    self.assertEqual(str(t),
"""
  3 8 8
4 6 8
  6 7 7
""")

  def testSeven(self):
    t = interval_tree.IntervalTree()
    t.insert(4, 6)
    t.insert(2, 5)
    t.insert(6, 7)
    t.insert(1, 1)
    t.insert(3, 4)
    t.insert(5, 9)
    t.insert(7, 8)
    self.assertEqual(t.search(3, 4), (4, 6))
    self.assertEqual(t.search(7, 7), (6, 7))
    self.assertEqual(str(t),
"""
    1 1 1
  2 5 5
    3 4 4
4 6 9
    5 9 9
  6 7 9
    7 8 8
""")


if __name__ == '__main__':
  unittest.main()