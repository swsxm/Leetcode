from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        max_val = nums[0]
        for i in range(2, len(nums)):
            max_val = max(max_val, nums[i - 2])
            if max_val > nums[i]:
                return False
        return True
