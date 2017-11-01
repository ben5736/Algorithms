import unittest

import trie

class TrieTest(unittest.TestCase):

    def testEmptyTrie(self):
        t = trie.Trie()
        self.assertEqual(t.GetWordsWithPrefix(''), [])
        self.assertEqual(t.GetWordsWithPrefix('foo'), [])

    def testOneWords(self):
        t = trie.Trie()
        t.Insert('cross')
        self.assertEqual(t.GetWordsWithPrefix('cr'), ['cross'])
        self.assertEqual(t.GetWordsWithPrefix(''), ['cross'])
        self.assertEqual(t.GetWordsWithPrefix('cross'), ['cross'])
    
    def testManyWords(self):
        t = trie.Trie()
        t.Insert('cross')
        t.Insert('crash')
        t.Insert('apple')
        t.Insert('cause')

        self.assertEqual(sorted(t.GetWordsWithPrefix('cross')), sorted(['cross']))
        self.assertEqual(sorted(t.GetWordsWithPrefix('cr')), sorted(['cross', 'crash']))
        self.assertEqual(sorted(t.GetWordsWithPrefix('c')), sorted(['cross', 'crash', 'cause']))
        self.assertEqual(sorted(t.GetWordsWithPrefix('')), sorted(['cross', 'crash', 'cause', 'apple']))

    def testRemove(self):
        t = trie.Trie()
        t.Insert('cross')
        t.Insert('crash')
        t.Insert('apple')

        with self.assertRaises(Exception):
            t.Remove('cruel')
        t.Remove('cross')
        self.assertEqual(sorted(t.GetWordsWithPrefix('')), ['apple', 'crash'])
        t.Remove('crash')
        self.assertEqual(t.GetWordsWithPrefix(''), ['apple'])


if __name__ == '__main__':
    unittest.main()
