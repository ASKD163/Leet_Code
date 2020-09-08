class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        def DFS(tmp,nums):
            if len(tmp) == k:
                res.append(tmp)
                return

            for i in range(len(nums)):
                DFS(tmp+[nums[i]],nums[i+1:])
                    
        res = []
        DFS([],nums)
        return res
