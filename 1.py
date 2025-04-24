from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lookup:
                return [i, lookup[diff]]
            lookup[nums[i]] = i
