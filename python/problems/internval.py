def removeElementFromIntervals(intervals, index):
  ret = []
  intervals = sorted(intervals)

  for interval in intervals:
    start, end = interval
    length = end - start + 1

    if index == -1:
      ret.append(interval)
    elif index >= length:
      index -= length
      ret.append(interval)
    else:
      if length == 1:
        pass # just skip this single element interval
      elif index == 0:
        ret.append((start + 1, end))
      elif index == length - 1:
        ret.append((start, end - 1))
      else:
        ret.append((start, start + index - 1))
        ret.append((start + index + 1, end))

      index = -1
  return ret

import unittest

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(removeElementFromIntervals([(4, 7), (10, 11), (13, 15)], 2), [(4, 5), (7,7), (10, 11), (13, 15)])
    self.assertEqual(removeElementFromIntervals([(4, 7), (10, 11), (13, 15)], 4), [(4, 7), (11, 11), (13, 15)])
    self.assertEqual(removeElementFromIntervals([(4, 7), (11, 11), (13, 15)], 4), [(4, 7), (13, 15)])

if __name__ == '__main__':
    unittest.main()