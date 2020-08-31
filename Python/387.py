class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for inx, i in enumerate(s):
            if d.get(i) == 1:
                return inx
        return -1
