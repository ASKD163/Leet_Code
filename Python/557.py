#反转字符串中的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        j = 0
        res = ''
        for inx,i in enumerate(s):
            if i == ' ':
                tmp = s[j:inx]
                j = inx + 1
                res = res + tmp[::-1] + ' '
            elif inx == (len(s)-1):
                tmp = s[j:inx+1]
                res = res + tmp[::-1]
            else:
                continue
        return res
        
############切片##############
class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join(s.split(' ')[::-1]))[::-1]
