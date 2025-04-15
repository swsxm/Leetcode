from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        lookup = set()
        for i in range(len(nums)):
            if nums[i] not in lookup:
                nums[index] = nums[i]
                index += 1
            lookup.add(nums[i])
        return index
