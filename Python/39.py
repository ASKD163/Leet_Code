class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(tmp,sum_t):
            if sum_t == target:
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            elif sum_t > target:
                return
            for i in candidates:
                DFS(tmp + [i],sum_t + i)

        res = []
        DFS([],0)
        
        return res 


##剪枝
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(tmp,sum_t,i):
            if sum_t == target:
                res.append(tmp)
                return

            for i in range(i,len(candidates)):
                if sum_t + candidates[i] <= target:
                    DFS(tmp + [candidates[i]],sum_t + candidates[i],i)

        res = []
        DFS([],0,0)
        
        return res
