class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] > threshold or nums[i] % 2 != 0:
                i += 1
                continue

            j = i + 1
            while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                j += 1

            max_length = max(max_length, j - i)
            i = j

        return max_length
