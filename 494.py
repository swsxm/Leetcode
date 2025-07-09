from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        lookup = {}

        def dfs(sum_, index):
            if index == len(nums):
                return 1 if sum_ == target else 0

            if (index, sum_) in lookup:
                return lookup[(index, sum_)]

            left = dfs(sum_ + nums[index], index + 1)  # add the element as positive
            right = dfs(sum_ - nums[index], index + 1)  # add the element as negative
            lookup[(index, sum_)] = left + right
            return lookup[(index, sum_)]

        return dfs(0, 0)
