from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        flip_index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[flip_index - 2]:
                nums[flip_index] = nums[i]
                flip_index += 1
        return flip_index
