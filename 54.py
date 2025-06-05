from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottem = len(matrix) - 1
        res = []

        while left <= right and top <= bottem:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottem + 1):
                res.append(matrix[i][right])
            right -= 1

            if top > bottem or left > right:
                break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottem][i])
            bottem -= 1

            for i in range(bottem, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
