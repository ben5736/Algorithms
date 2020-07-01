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
5 1

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
4 5

0 4
1 1

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
5 1

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

  def testSolve1(self):
    c = cube.Cube()
    c.move('right_clockwise')
    c.move('right_clockwise')
    c.move('right_clockwise')
    self.assertEqual(c.solveDFS(), ['right_clockwise'])

  def testSolve2(self):
    c = cube.Cube()
    c.move('right_clockwise')
    c.move('right_clockwise')
    self.assertEqual(c.solveDFS(), ['right_clockwise', 'right_clockwise'])


if __name__ == '__main__':
  unittest.main()
