class Solution:
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n ** 2)
        for _ in range(k):
            last = nums[-1]
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n)
        lookup = nums[:]
        for i in range(len(lookup)):
            new_index = (i + k) % len(nums)
            nums[new_index] = lookup[i]
