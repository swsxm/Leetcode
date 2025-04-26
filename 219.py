from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False


Test = Solution()
print(Test.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
