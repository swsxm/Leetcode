from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
