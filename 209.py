from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        l, r = 0, 0
        curr_sum = 0
        while r < len(nums) and l <= r:
            if curr_sum >= target:
                min_len = min(r - l, min_len)
                curr_sum -= nums[l]
                l += 1
            else:
                curr_sum += nums[r]
                r += 1
        while curr_sum >= target and l < r:
            min_len = min(min_len, r - l)
            curr_sum -= nums[l]
            l += 1
        return 0 if min_len > len(nums) else min_len
