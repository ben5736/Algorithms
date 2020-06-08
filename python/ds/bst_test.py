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
    self.assertEqual(str(t), '3')

    t.delete(3)
    self.assertEqual(t.search(3), False)
    self.assertEqual(str(t), '')

  def testTwoElementBST(self):
    t = bst.BST()
    t.insert(3)
    t.insert(5)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(5), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '3 [5]')

    t.delete(3)
    self.assertEqual(t.search(3), False)
    self.assertEqual(str(t), '5')

  def testThreeElementBST(self):
    t = bst.BST()
    t.insert(3)
    t.insert(5)
    t.insert(1)
    self.assertEqual(t.search(3), True)
    self.assertEqual(t.search(5), True)
    self.assertEqual(t.search(1), True)
    self.assertEqual(t.search(0), False)
    self.assertEqual(str(t), '[1] 3 [5]')

    t.delete(3)
    self.assertEqual(str(t), '1 [5]')

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
    self.assertEqual(str(t), '[1 [2]] 3 [5]')

    t.delete(3)
    self.assertEqual(str(t), '[1] 2 [5]')

  def testRightPath(self):
    t = bst.BST()
    t.insert(5)
    t.insert(6)
    t.insert(7)
    self.assertEqual(str(t), '5 [6 [7]]')

    t.delete(6)
    self.assertEqual(str(t), '5 [7]')

  def testDeleteNonexistent(self):
    t = bst.BST()
    t.insert(3)
    self.assertRaises(Exception, lambda: t.delete(4))

  def testComplete(self):
    t = bst.BST()
    t.insert(5)
    t.insert(2)
    t.insert(7)
    t.insert(1)
    t.insert(3)
    t.insert(6)
    t.insert(8)
    t.insert(4)
    self.assertEqual(str(t), '[[1] 2 [3 [4]]] 5 [[6] 7 [8]]')

    t.delete(5)
    self.assertEqual(str(t), '[[1] 2 [3]] 4 [[6] 7 [8]]')

    t.delete(8)
    self.assertEqual(str(t), '[[1] 2 [3]] 4 [[6] 7]')

    t.delete(7)
    self.assertEqual(str(t), '[[1] 2 [3]] 4 [6]')

    t.delete(1)
    self.assertEqual(str(t), '[2 [3]] 4 [6]')

if __name__ == '__main__':
  unittest.main()