class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def DFS(tmp,i):
            res.append(tmp)
            for i in range(i,len(nums)): 
                DFS(tmp+[nums[i]], i+1)

        res = []
        DFS([],0)
        return res
