#最短回文
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 1
        j = 0
        prefix = [0]
        tmp = s + '#'+ s[::-1]
        while i < len(tmp):
            if (tmp[i] == tmp[j]):
                j += 1 
                prefix.append(j)
                i += 1
            else:
                if j > 0:
                    j = prefix[j-1]
                else:
                    prefix.append(0)
                    i += 1
# KMP 计算 s+#+rev_s 的最大公共前后缀

        best = prefix[-1]
        rev = s[::-1]
        res = rev[:(len(s)-best)] + s #rev_s减去最大公共前后缀+s
        return res
