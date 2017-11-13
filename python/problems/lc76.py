import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ''

        all_chars = set(t)
        cur_chars = collections.defaultdict(int)
        start = 0
        end = 0
        minimal = None
        while start < len(s):
            print start, end, minimal, len(cur_chars)
            if len(cur_chars) < len(all_chars):
                if end < len(s):
                    if s[end] in all_chars:
                        cur_chars[end] += 1
                    end += 1
                else:
                    return minimal
            else:
                if minimal is None or end - start < len(minimal):
                    minimal = s[start:end]
                if s[start] in cur_chars:
                    cur_chars[s[start]] -= 1
                    if cur_chars[s[start]] == 0:
                        del cur_chars[s[start]]
                start += 1
        return minimal or ''

print Solution().minWindow('a', 'a')
