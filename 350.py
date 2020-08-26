//双指针

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        j = 0
        i = 0 
        while (i < len(nums1) )and( j < len(nums2)):   
                if nums1[i] == nums2[j]:
                    res.append(nums2[j])
                    j += 1
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    i+=1

        return res
