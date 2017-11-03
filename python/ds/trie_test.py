import unittest

import trie

class TrieTest(unittest.TestCase):

  def _AssertGetWordsWithAfix(self, trie, afix, expected):
    self.assertEqual(sorted(trie.GetWordsWithAfix(afix)), sorted(expected))

  def testEmptyTrie(self):
    t = trie.Trie()
    self._AssertGetWordsWithAfix(t, '', [])
    self._AssertGetWordsWithAfix(t, 'foo', [])

  def testOneWords(self):
    t = trie.Trie()
    t.Insert('cross')
    self._AssertGetWordsWithAfix(t, 'cr', ['cross'])
    self._AssertGetWordsWithAfix(t, '', ['cross'])
    self._AssertGetWordsWithAfix(t, 'cross', ['cross'])

  def testManyWords(self):
    t = trie.Trie()
    t.Insert('cross')
    t.Insert('crash')
    t.Insert('apple')
    t.Insert('cause')

    self._AssertGetWordsWithAfix(t, 'cross', ['cross'])
    self._AssertGetWordsWithAfix(t, 'cr', ['cross', 'crash'])
    self._AssertGetWordsWithAfix(t, 'c', ['cross', 'crash', 'cause'])
    self._AssertGetWordsWithAfix(t, '', ['cross', 'crash', 'cause', 'apple'])

  def testRemove(self):
    t = trie.Trie()
    t.Insert('cross')
    t.Insert('crash')
    t.Insert('apple')

    with self.assertRaises(Exception):
      t.Remove('cruel')
    t.Remove('cross')
    self._AssertGetWordsWithAfix(t, '', ['apple', 'crash'])
    t.Remove('crash')
    self._AssertGetWordsWithAfix(t, '', ['apple'])

  def testSuffix(self):
    t = trie.Trie(is_suffix=True)
    t.Insert('crew')
    t.Insert('drew')
    self._AssertGetWordsWithAfix(t, 'ew', ['crew', 'drew'])
    self._AssertGetWordsWithAfix(t, 'crew', ['crew'])

    t.Remove('crew')
    self._AssertGetWordsWithAfix(t, 'ew', ['drew'])



if __name__ == '__main__':
  unittest.main()
