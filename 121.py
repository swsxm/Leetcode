from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]

        for price in prices:
            profit = max(profit, price - minimum)
            minimum = min(minimum, price)
        return profit
