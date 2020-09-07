class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = collections.Counter(nums)#hash table 计数
        count = sorted(count.items(), key = lambda d:d[1], reverse = True) #按value排序，转list
                                                                           #list.sort(cmp=None, key=None, reverse=False)
        for i in count:
            res.append(i[0])
            if len(res) == k:
                return res
