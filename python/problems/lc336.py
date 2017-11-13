import collections
from ds import trie

class Solution(object):
  def isPalindrome(self, word):
    s = 0
    e = len(word) - 1
    while e > s:
      if word[s] != word[e]:
        return False
      s += 1
      e -= 1
    return True

  def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    prefix_trie = trie.Trie()
    suffix_trie = trie.Trie(is_suffix=True)
    index_map = {}

    for i, w in enumerate(words):
      prefix_trie.Insert(w)
      suffix_trie.Insert(w)
      index_map[w] = i

    ret = []

    for i, w in enumerate(words):
      possible_suffix = suffix_trie.GetWordsWithAfix(w[::-1])
      for suffix in possible_suffix:
        if self.isPalindrome(suffix[:-len(w)]) and (len(w) != len(suffix) or i < index_map[suffix]):
          ret.append([i, index_map[suffix]])
      possible_prefix = prefix_trie.GetWordsWithAfix(w[::-1])
      for prefix in possible_prefix:
        if self.isPalindrome(prefix[len(w):]) and (len(w) != len(prefix) or i < index_map[prefix]):
          ret.append([index_map[prefix], i])
      print ret
    return ret

print Solution().palindromePairs(["abcd","dcba","lls","s","sssll", 'aba'])
