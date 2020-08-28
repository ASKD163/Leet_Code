#两数之和
#暴力搜索
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    res.append(i)
                    res.append(j)
        return res
        
        
####################
#哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for inx,i in enumerate(nums):
            if (target - i) in hashmap:
                return [inx, hashmap.get(target - i)]
            hashmap[i] = inx
