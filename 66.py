from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        end = len(digits) - 1
        while end >= 0 and carry:
            digits[end] = (digits[end] + 1) % 10
            carry = 1 if digits[end] == 0 else 0
            end -= 1
        if carry:
            return [1] + digits
        return digits
