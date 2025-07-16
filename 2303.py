from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0.0
        prev = 0
        for upper, percent in brackets:
            if income > prev:
                money_to_tax = min(income, upper) - prev
                taxes += money_to_tax * percent / 100
                prev = upper
            else:
                break

        return taxes
