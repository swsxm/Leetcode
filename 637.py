# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        ret = []

        while stack:
            length = len(stack)
            new_nodes = []  # or use deque
            sum_lvl = 0
            for node in stack:
                sum_lvl += node.val
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            stack = new_nodes
            ret.append(sum_lvl / length)
        return ret
