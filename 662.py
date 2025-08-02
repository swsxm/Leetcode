from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = deque([(0, root)])
        max_width = 1
        while nodes:
            if len(nodes) > 1:
                width = nodes[-1][0] + (-1 * nodes[0][0])
                max_width = max(width + 1, max_width)
            for _ in range(len(nodes)):
                idx, node = nodes.popleft()
                if node.left:
                    nodes.append((idx * 2 + 1, node.left))
                if node.right:
                    nodes.append((idx * 2 + 2, node.right))
        return max_width
