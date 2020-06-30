class Cube(object):

  def __init__(self, faces=None):
    def __makeFace(val):
      return [[val, val], [val, val]]
    if not faces:
      self._front = __makeFace(0)
      self._top = __makeFace(1)
      self._right = __makeFace(2)
      self._bottom = __makeFace(3)
      self._left = __makeFace(4)
      self._back = __makeFace(5)
    else:
      self._front, self._top, self._right, self._bottom, self._left, self._back = faces

  def _faceSolved(self, face):
    first = face[0][0]
    for i in xrange(len(face)):
      for j in xrange(len(face)):
        if face[i][j] != first:
          return False
    return True

  def solved(self):
    return (self._faceSolved(self._front)
      and self._faceSolved(self._top)
      and self._faceSolved(self._right)
      and self._faceSolved(self._bottom)
      and self._faceSolved(self._left)
      and self._faceSolved(self._back))

  def _faceStr(self, face):
    return '%d %d\n%d %d\n' % (face[0][0], face[0][1], face[1][0], face[1][1])

  def __str__(self):
    return '\n'.join([
      self._faceStr(self._front),
      self._faceStr(self._top),
      self._faceStr(self._right),
      self._faceStr(self._bottom),
      self._faceStr(self._left),
      self._faceStr(self._back)
      ])

  def supportedMoves(self):
    return ['right_clockwise', 'bottom_clockwise', 'back_clockwise']

  def _rotateFaceClockwise(self, face):
    tmp = face[0][0]
    face[0][0] = face[1][0]
    face[1][0] = face[1][1]
    face[1][1] = face[0][1]
    face[0][1] = tmp

  def move(self, moveStr):
    if moveStr not in self.supportedMoves():
      raise Exception('Unsupported move.')
    if moveStr == 'right_clockwise':
      self._rotateFaceClockwise(self._right)
      tmp1, tmp2 = self._front[0][1], self._front[1][1]
      self._front[0][1], self._front[1][1] = self._bottom[0][1], self._bottom[1][1]
      self._bottom[0][1], self._bottom[1][1] = self._back[0][1], self._back[1][1]
      self._back[0][1], self._back[1][1] = self._top[0][1], self._top[1][1]
      self._top[0][1], self._top[1][1] = tmp1, tmp2
    elif moveStr == 'bottom_clockwise':
      self._rotateFaceClockwise(self._bottom)
      tmp1, tmp2 = self._front[1][0], self._front[1][1]
      self._front[1][0], self._front[1][1] = self._left[1][0], self._left[1][1]
      self._left[1][0], self._left[1][1] = self._back[0][0], self._back[0][1]
      self._back[0][0], self._back[0][1] = self._right[1][1], self._right[1][0]
      self._right[1][0], self._right[1][1] = tmp1, tmp2
    else:
      self._rotateFaceClockwise(self._back)
      tmp1, tmp2 = self._top[0][0], self._top[0][1]
      self._top[0][0], self._top[0][1] = self._right[0][1], self._right[1][1]
      self._right[0][1], self._right[1][1] = self._bottom[1][1], self._bottom[1][0]
      self._bottom[1][0], self._bottom[1][1] = self._left[0][0], self._left[1][0]
      self._left[0][0], self._left[1][0] = tmp2, tmp1