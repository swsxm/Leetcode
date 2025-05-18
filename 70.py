class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def step(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            else:
                memo[n] = step(n - 1) + step(n - 2)
                return memo[n]

        return step(n)
