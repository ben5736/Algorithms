_DELIMITER = ';'
_ESCAPER = ':'

def encode(input):
  return _DELIMITER.join([encode_segment(segment) for segment in input])

def encode_segment(segment):
  ret = ''
  for c in segment:
    if c == _DELIMITER:
      ret += _ESCAPER + _DELIMITER
    elif c == _ESCAPER:
      ret += _ESCAPER + _ESCAPER
    else:
      ret += c
  return ret

def decode(input):
  ret = []
  cur = ''
  i = 0
  while i < len(input):
    c = input[i]
    if c == _DELIMITER:
      ret.append(cur)
      cur = ''
    elif c == _ESCAPER:
      cur += input[i + 1]
      i += 1
    else:
      cur += c
    i += 1
  ret.append(cur)
  return ret

import unittest

class Test(unittest.TestCase):

  def test1(self):
    input = ['abc', 'def', 'ghi']
    self.assertEqual(decode(encode(input)), input)

  def test2(self):
    input = ['a:c', 'd;f', 'g//i']
    self.assertEqual(decode(encode(input)), input)

if __name__ == '__main__':
    unittest.main()