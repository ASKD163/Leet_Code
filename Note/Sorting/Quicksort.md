# Quick Sort
**Divide and Conquer** 思想，将要排列的数组```nums```以```pivot```为间隔切分为两段，左边小于```pivot```右边大于```pivot```，不断迭代直至小段长度小于2

**keystep** ```partition```使用双指针（i 指向-1， j）遍历数组，若```nums[j]``` 小于或等于```nums[-1]```,i加一，```nums[i]```,```nums[j]```换位，最后```nums[i+1]```与```nums[-1]```换位

```python
def quicksort(nums: list, l: int, r: int):
    if l < r:
        q = partition(nums,l,r) # pivot
        quicksort(nums, l, q-1)
        quicksort(nums, q+1, r)
    return nums

def partition(nums: list, l: int, r: int) -> int:
    x = nums[r]
    i = l - 1
    for j in range(l,r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1
```
