class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        res = ''
        l = 1
        k -= 1
        while len(res) < n:
            i = k // factorial(n-l)
            k = k %factorial(n-l)
            l += 1
            res += str(nums[i])
            nums = nums[:i] + nums[i+1:]
            
        return res
