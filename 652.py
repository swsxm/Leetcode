from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        nodes = []
        count = defaultdict(int)
        NULL = None

        def dfs(node):
            if not node:
                return NULL
            L = dfs(node.left)
            R = dfs(node.right)
            sig = (node.val, L, R)
            count[sig] += 1
            if count[sig] == 2:
                nodes.append(node)
            return sig

        dfs(root)
        return nodes
