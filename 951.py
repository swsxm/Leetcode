from typing import Optional
import polars as pl
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse_it(test_2, root2):
            if test_2 is None and root2 is None:
                return True
            if test_2 is None or root2 is None:
                return False
            if test_2.val != root2.val:
                return False

            return (
                traverse_it(test_2.left, root2.left) and traverse_it(test_2.right, test_2.right)
            ) or (
                traverse_it(test_2.left, root2.right) and traverse_it(test_2.right, root2.left)
            )

        return traverse_it()


df = pl.DataFrame() 
