from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        # not done
        m, n = len(grid), len(grid[0])

        base_flips = 0

        for i in range(m // 2):
            for j in range(n // 2):
                s = (
                    grid[i][j]
                    + grid[i][n - 1 - j]
                    + grid[m - 1 - i][j]
                    + grid[m - 1 - i][n - 1 - j]
                )
                base_flips += min(s, 4 - s)

        mixed_pairs = 0
        ones_pairs = 0
        zeros_pairs = 0

        if m % 2 == 1:
            i = m // 2
            for j in range(n // 2):
                a = grid[i][j]
                b = grid[i][n - 1 - j]
                s = a + b
                if s == 1:
                    mixed_pairs += 1
                    base_flips += 1
                elif s == 2:
                    ones_pairs += 1
                else:
                    zeros_pairs += 1

        if n % 2 == 1:
            j = n // 2
            for i in range(m // 2):
                a = grid[i][j]
                b = grid[m - 1 - i][j]
                s = a + b
                if s == 1:
                    mixed_pairs += 1
                    base_flips += 1
                elif s == 2:
                    ones_pairs += 1
                else:  # s == 0
                    zeros_pairs += 1

        if m % 2 == 1 and n % 2 == 1:
            i, j = m // 2, n // 2
            v = grid[i][j]
            base_flips += min(v, 1 - v)

        can_make_mod0_for_free = False
        if mixed_pairs > 0:
            can_make_mod0_for_free = True
        else:
            if ones_pairs % 2 == 0:
                can_make_mod0_for_free = True

        if can_make_mod0_for_free:
            return base_flips
        else:
            return base_flips + 2
