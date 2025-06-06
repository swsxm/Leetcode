from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        SIZE = len(matrix) - 1
        l, t = 0, 0
        n = len(matrix)

        while l < n // 2:
            b = SIZE - t
            r = SIZE - l

            for i in range(0, r - l):
                tmp = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = tmp

            l += 1
            t = l
