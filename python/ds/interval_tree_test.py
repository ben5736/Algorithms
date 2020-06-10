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
    t.delete(2, 4)
    self.assertEqual(str(t), 
"""

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
    t.delete(3, 6)
    self.assertEqual(str(t),
"""
2 4 4
""")
    t.delete(2, 4)
    self.assertEqual(str(t), 
"""

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
    t.delete(4, 6)
    self.assertEqual(str(t),
"""
3 8 8
  6 7 7
""")
    t.delete(3, 8)
    self.assertEqual(str(t),
"""
6 7 7
""")

  def testSeven(self):
    t = interval_tree.IntervalTree()
    t.insert(4, 6)
    t.insert(2, 5)
    t.insert(6, 7)
    t.insert(1, 1)
    t.insert(3, 10)
    t.insert(5, 9)
    t.insert(7, 8)
    self.assertEqual(t.search(3, 4), (4, 6))
    self.assertEqual(t.search(7, 7), (3, 10))
    self.assertEqual(str(t),
"""
    1 1 1
  2 5 10
    3 10 10
4 6 10
    5 9 9
  6 7 9
    7 8 8
""")
    t.delete(4, 6)
    self.assertEqual(str(t),
"""
    1 1 1
  2 5 5
3 10 10
    5 9 9
  6 7 9
    7 8 8
""")
    t.delete(6, 7)
    self.assertEqual(str(t),
"""
    1 1 1
  2 5 5
3 10 10
  5 9 9
    7 8 8
""")
    t.delete(2, 5)
    self.assertEqual(str(t),
"""
  1 1 1
3 10 10
  5 9 9
    7 8 8
""")
    t.delete(3, 10)
    self.assertEqual(str(t),
"""
1 1 9
  5 9 9
    7 8 8
""")
    self.assertRaises(Exception, lambda:t.delete(1, 3))

  def testSwapDelete(self):
    t = interval_tree.IntervalTree()
    t.insert(6, 7)
    t.insert(7, 8)
    t.insert(3, 10)
    t.insert(4, 6)
    t.insert(2, 5)
    t.insert(1, 1)
    t.insert(5, 9)
    self.assertEqual(str(t),
"""
      1 1 1
    2 5 5
  3 10 10
    4 6 9
      5 9 9
6 7 10
  7 8 8
""")
    t.delete(6, 7)
    self.assertEqual(str(t),
"""
      1 1 1
    2 5 5
  3 10 10
    4 6 6
5 9 10
  7 8 8
""")

if __name__ == '__main__':
  unittest.main()