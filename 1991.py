from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = len(nums)
        prefix = [0] * s
        postfix = [0] * s
        sum = 0
        for i in range(0, s):
            prefix[i] = sum
            sum += nums[i]
        sum = 0
        for i in range(s - 1, -1, -1):
            postfix[i] = sum
            sum += nums[i]
        for i in range(s):
            if postfix[i] == prefix[i]:
                return i
        return -1

    def findMiddleIndex2(self, nums):
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        return -1


test = Solution()
print(test.findMiddleIndex([2, 3, -1, 8, 4]))
