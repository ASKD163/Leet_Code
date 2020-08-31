class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        res = 0
        while y>0:
            res = res*10 + y%10
            y = y//10
            if res > (2**31)-1:
                return 0
        return res if x>0 else -res
