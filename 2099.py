from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_w_index = list(enumerate(nums))
        sorted_by_val = sorted(nums_w_index, key=lambda x: x[1], reverse=True)[:k]
        sorted_by_index = sorted(sorted_by_val, key=lambda x: x[0])
        return [tuple[1] for tuple in sorted_by_index]


Test = Solution()
print(Test.maxSubsequence([50, -75], 2))
