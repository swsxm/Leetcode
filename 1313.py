from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        dc = []
        for i in range(0, len(nums) - 1, 2):
            dc += [nums[i + 1]] * nums[i]
        return dc
