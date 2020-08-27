class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        while i:
            digits[-i] += 1
            if digits[-i] == 10:
                digits[-i] = 0
                if i == len(digits):
                    digits.insert(0,0)
                i += 1
            else:
                i = 0

        return digits
