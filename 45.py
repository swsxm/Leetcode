from typing import List


class Solution:
    def jump1(self, nums: List[int]) -> int:
        count = 0
        max_reach = 0
        min_reach = 0
        while max_reach < len(nums) - 1:
            count += 1
            next_reach = max(i + nums[i] for i in range(min_reach, max_reach + 1))
            min_reach = max_reach + 1
            max_reach = next_reach

        return count

    def jump(self, nums: List[int]) -> int:
        count = 0
        max_reach = 0
        current_end = 0
        for i in range(len(nums) - 1):
            max_reach = max(nums[i] + i, max_reach)
            if i == current_end:
                count += 1
                current_end = max_reach
        return count
