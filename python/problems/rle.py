def encode(input):
  ret = ''
  cur = ''
  count = 0
  for s in input:
    if s == cur:
      count += 1
    else:
      if cur != '':
        ret += cur
        ret += str(count)
      cur = s
      count = 1
  if cur != '':
    ret += cur
    ret += str(count)
  return ret

def decode(input):
  ret = ''
  i = 0
  while i < len(input):
    char = input[i]
    count, i = extract_count(input, i + 1)
    for _ in range(count):
      ret += char
  return ret

def extract_count(input, i):
  start = i
  end = i + 1
  while end < len(input) and input[end].isdigit():
    end += 1
  return int(input[start:end]), end

import unittest

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(encode("AAABBCDDD"), "A3B2C1D3")

  def test2(self):
    self.assertEqual(decode("A3B2C13A5"), "AAABBCCCCCCCCCCCCCAAAAA")

if __name__ == '__main__':
    unittest.main()