from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = max(nums)
        return sorted(nums) == list(range(1, base + 1)) + [base]
