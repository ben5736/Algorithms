import unittest

import bst

class BSTTest(unittest.TestCase):

  def testEmptyBST(self):
    t = bst.BST()
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '')

  def testOneElementBST(self):
    t = bst.BST()
    t.insert(3)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '[] 3 []')

  def testTwoElementBST(self):
    t = bst.BST()
    t.insert(3)
    t.insert(5)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(5), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '[] 3 [[] 5 []]')

  def testThreeElementBST(self):
    t = bst.BST()
    t.insert(3)
    t.insert(5)
    t.insert(1)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(5), True)
    self.assertEqual(t.search(1), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '[[] 1 []] 3 [[] 5 []]')

  def testFourElementBST(self):
    t = bst.BST()
    t.insert(3)
    t.insert(5)
    t.insert(1)
    t.insert(2)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(5), True)
    self.assertEqual(t.search(1), True)
    self.assertEqual(t.search(2), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '[[] 1 [[] 2 []]] 3 [[] 5 []]')


if __name__ == '__main__':
  unittest.main()