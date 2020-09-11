class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def search(tmp,sum_t,i):
            if sum_t == n and len(tmp) == k:
                res.append(tmp)
                return 
            for i in range(i,9):
                if sum_t + nums[i] <= n and len(tmp) + 1 <= k:
                    search(tmp + [nums[i]], sum_t+nums[i],i+1)

        nums = [ i for i in range(1,10)]
        res = []
        search([],0,0)
        return res 

##################
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def search(tmp,sum_t,i):
            if sum_t == 0 and len(tmp) == k:
                res.append(tmp)
                return
            if sum_t < 0:
                return
            if len(tmp) > k:
                return
            if i == 10:
                return
            search(tmp + [i],sum_t - i, i+1)
            search(tmp, sum_t, i+1)
            
        res = [] 
        search([],n,1)
        return res 
