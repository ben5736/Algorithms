import unittest

import cube

class CubeTest(unittest.TestCase):

  def _assertCubeEqual(self, c, cstr):
    self.assertEqual('\n' + str(c), cstr)

  def testInit(self):
    c = cube.Cube()
    self._assertCubeEqual(c,
"""
0 0
0 0

1 1
1 1

2 2
2 2

3 3
3 3

4 4
4 4

5 5
5 5
""")

  def testMove(self):
    c = cube.Cube()
    c.move('right_clockwise')
    self._assertCubeEqual(c,
"""
0 3
0 3

1 0
1 0

2 2
2 2

3 5
3 5

4 4
4 4

5 1
5 1
""")

    c.move('bottom_clockwise')
    self._assertCubeEqual(c,
"""
0 3
4 4

1 0
1 0

2 2
0 3

3 3
5 5

4 4
1 5

2 2
5 1
""")

    c.move('back_clockwise')
    self._assertCubeEqual(c,
"""
0 3
4 4

2 3
1 0

2 5
0 5

3 3
4 1

0 4
1 5

5 2
1 2
""")

  def testCopy(self):
    c1 = cube.Cube()
    c1.move('right_clockwise')
    c2 = c1.copy()
    self._assertCubeEqual(c2,
"""
0 3
0 3

1 0
1 0

2 2
2 2

3 5
3 5

4 4
4 4

5 1
5 1
""")

    c2.move('bottom_clockwise')
    self._assertCubeEqual(c2,
"""
0 3
4 4

1 0
1 0

2 2
0 3

3 3
5 5

4 4
1 5

2 2
5 1
""")

    self._assertCubeEqual(c1,
"""
0 3
0 3

1 0
1 0

2 2
2 2

3 5
3 5

4 4
4 4

5 1
5 1
""")

  def testBottomClockwiseMove(self):
    c = cube.Cube()
    c.move('right_clockwise')
    self._assertCubeEqual(c,
"""
0 3
0 3

1 0
1 0

2 2
2 2

3 5
3 5

4 4
4 4

5 1
5 1
""")

    c.move('bottom_clockwise')
    self._assertCubeEqual(c,
"""
0 3
4 4

1 0
1 0

2 2
0 3

3 3
5 5

4 4
1 5

2 2
5 1
""")

  def testSolveDFS1(self):
    c = cube.Cube()
    c.move('right_clockwise')
    c.move('right_clockwise')
    c.move('right_clockwise')
    self.assertEqual(c.solveDFS(), ['right_clockwise'])

  def testSolveDFS2(self):
    c = cube.Cube()
    c.move('right_clockwise')
    c.move('right_clockwise')
    self.assertEqual(c.solveDFS(), ['right_clockwise', 'right_clockwise'])

  def testMoves(self):
    c = cube.Cube()
    c.move('right_clockwise')
    self.assertFalse(c.solved())
    c.move('right_counterclockwise')
    self.assertTrue(c.solved())

    c.move('bottom_clockwise')
    self.assertFalse(c.solved())
    c.move('bottom_counterclockwise')
    self.assertTrue(c.solved())

    c.move('back_clockwise')
    self.assertFalse(c.solved())
    c.move('back_counterclockwise')
    self.assertTrue(c.solved())

  def testUnmoves1(self):
    c = cube.Cube()
    for move in c.supportedMoves():
      c.move(move)
      self.assertFalse(c.solved())
      c.unmove(move)
      self.assertTrue(c.solved())

  def testUnmoves2(self):
    c = cube.Cube()
    c.move('right_clockwise')
    copy = c.copy()
    for move in c.supportedMoves():
      c.move(move)
      self.assertNotEqual(str(c), str(copy))
      c.unmove(move)
      self.assertEqual(str(c), str(copy))

  def testSolveBFS1(self):
    c = cube.Cube()
    c.move('right_clockwise')
    self.assertEqual(c.solveBFS(), ['right_counterclockwise'])

  def testSolveBFS2(self):
    c = cube.Cube()
    c.move('right_clockwise')
    c.move('right_clockwise')
    c.move('back_counterclockwise')
    c.move('bottom_clockwise')
    actual = c.solveBFS()
    self.assertEqual(actual, ['bottom_counterclockwise', 'back_clockwise', 'right_clockwise', 'right_clockwise'])  


if __name__ == '__main__':
  unittest.main()
