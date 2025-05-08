# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float("inf")

        def helper(root):
            nonlocal min_diff, prev
            if not root:
                return
            helper(root.left)
            if prev is not None:
                min_diff = min(abs(prev - root.val), min_diff)
            prev = root.val
            helper(root.right)

        helper(root)
        return min_diff
