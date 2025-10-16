from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0 or not matchsticks:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse=True)
        square = [0, 0, 0, 0]

        def brute_force(i: int) -> bool:
            if i == len(matchsticks):
                return all(side == target for side in square)

            stick = matchsticks[i]
            seen_empty = False  
            for pos in range(4):
                if square[pos] + stick > target:
                    continue
                if square[pos] == 0 and seen_empty:
                    continue
                square[pos] += stick
                if brute_force(i + 1):
                    return True
                square[pos] -= stick
                if square[pos] == 0:
                    seen_empty = True
            return False

        return brute_force(0)
