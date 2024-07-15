def delete_helper(ref, cover, i):
  cur = 0
  for j in range(len(cover)): 
    seg = cover[j]
    start, end = seg
    length = end - start
    if i >= cur + length:
      cur += length
    else:  # i in current seg
      ret = []
      i_pos = i - cur + start
      new_end = i_pos
      new_start = i_pos + 1
      if new_end > start:
        ret.append((start, new_end))
      if end > new_start:
        ret.append((new_start, end))
      return j, ret

def delete(ref, cover, i):
  pos, segs = delete_helper(ref, cover, i)
  candidates = []
  if pos - 1 >= 0:
    candidates.append(cover[pos - 1])
  candidates += segs
  if pos + 1 < len(cover):
    candidates.append(cover[pos + 1])
  merged = tryMergeMultiple(ref, candidates)
  ret = []
  if pos - 1 >= 0:
    ret += cover[0:pos - 1]
  ret += merged
  if pos + 2 < len(cover):
    ret += cover[pos + 2:]
  return ret

def tryMergeMultiple(ref, segs):
  for i in range(len(segs) - 1):
    merged = tryMerge(ref, segs[i], segs[i + 1])
    if merged is not None:
      all_segs = segs[0:i] + [merged] + (segs[i+2:] if i + 2 < len(segs) else [])
      return tryMergeMultiple(ref, all_segs)
  return segs

def tryMerge(ref, seg1, seg2):
  seg1_start, seg1_end = seg1
  seg2_start, seg2_end = seg2
  seg1_len = seg1_end - seg1_start
  seg2_len = seg2_end - seg2_start
  if seg1_len + seg2_len > ref:
    return None
  if seg1_end + seg2_len <= len(ref) and ref[seg1_end:seg1_end + seg2_len] == ref[seg2_start:seg2_end]:
    return (seg1_start, seg1_end + seg2_len)
  tar = ref[seg1_start:seg1_end] + ref[seg2_start:seg2_end]
  start = ref.find(tar)
  if start >= 0:
    return start, start + len(tar)
  else:
    return None


import unittest

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(delete('abc1234abcd', [(3, 5), (7, 11), (3, 6)], 5), [(3, 5), (0, 6)])
    self.assertEqual(delete('abc1234abcd', [(3, 5), (7, 11), (3, 6)], 6), [(3, 5), (7, 11), (4, 6)])
    self.assertEqual(delete('abc1234abcd', [(3, 5), (7, 11), (3, 6)], 4), [(3, 5), (7, 9), (10, 11), (3, 6)])
    self.assertEqual(delete('abc1234abcd', [(3, 5), (10, 11), (3, 6)], 2), [(3, 5), (3, 6)])
    self.assertEqual(delete('abc1234abcd', [(0, 4), (6, 7), (4, 7)], 4), [(0, 7)])

  def test2(self):
    self.assertEqual(tryMerge('abc1234abcd', (0, 3), (3, 5)), (0, 5))
    self.assertEqual(tryMerge('abc1234abcd', (7, 10), (3, 5)), (0, 5))
    self.assertEqual(tryMerge('abc1234abcd', (7, 11), (3, 5)), None)

if __name__ == '__main__':
    unittest.main()