from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        start, end = 0, len(nums)
        i = 0
        while start < end:
            while i + 1 < end and nums[i + 1] - nums[i] <= 1:
                i += 1
            if nums[start] == nums[i]:
                ret.append(f"{nums[start]}")
            else:
                ret.append(f"{nums[start]}->{nums[i]}")
            start = i + 1
            i += 1

        return ret
