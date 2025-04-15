from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > len(nums) / 2:
                return i

    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
