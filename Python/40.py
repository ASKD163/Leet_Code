class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(tmp,sum_t,candidates):
            if sum_t == target:
                res.append(tmp)
                return

            for i in range(len(candidates)):
                if i>0 and candidates[i] == candidates[i-1]: 
                    continue
                if sum_t + candidates[i] <= target:
                    DFS(tmp + [candidates[i]],sum_t + candidates[i],candidates[i+1:])

        candidates.sort()
        res = []
        DFS([],0,candidates)
        
        return res
