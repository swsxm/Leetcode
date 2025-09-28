class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if m > n:
            n, m = m, n
        if n > k:
            need_to_cut = n - k
            return need_to_cut * (n - need_to_cut)
        return 0
