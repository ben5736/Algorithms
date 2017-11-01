import collections

class TrieNode(object):

    def __init__(self):
        self._children = collections.defaultdict(TrieNode)
        self._is_terminal = False

class Trie(object):
    
    def __init__(self):
        self._root = TrieNode()

    def Insert(self, word):
        cur = self._root
        for c in word:
            cur = cur._children[c]
        cur._is_terminal = True

    def GetWordsWithPrefix(self, prefix):
        cur = self._root
        for c in prefix:
            cur = cur._children.get(c)
            if not cur:
                return []
        return [prefix + w for w in self._GetAllWords(cur)]
    
    def _GetAllWords(self, node):
        ret = []
        if node._is_terminal:
            ret.append('')
        for c, child in node._children.iteritems():
            all_child_words = self._GetAllWords(child)
            for word in all_child_words:
                ret.append(c + word)
        return ret

    def Remove(self, word):
        path = [self._root]
        cur = self._root
        for c in word:
            if c in cur._children:
                cur = cur._children[c]
                path.append(cur)
            else:
                raise Exception('Word %s not in current trie.' % word)
        cur._is_terminal = False
        for i in reversed(range(len(path))):
            if not path[i]._is_terminal and not path[i]._children and i > 0:
                del path[i - 1]._children[word[i - 1]]


