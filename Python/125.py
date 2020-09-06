class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = []
        for i in s:
            if i.isdigit():
                 S.append(i)
            elif i.isalpha():
                S.append(i.lower())
        if not S:
            return True
        j = len(S)-1
        i = 0
        while i < len(S)/2:
            if S[i] == S[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
