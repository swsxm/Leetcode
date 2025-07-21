import math


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_len = math.floor(math.log10(n)) + 1
        a_sum = 0
        # edge case n_len == 1
        # as we start from behind
        if n_len == 1:
            return n
        # this indicates the state
        # True = +, False = -
        state = False if n_len % 2 == 0 else True
        while n > 0:
            n, last_digit = divmod(n, 10)
            a_sum += +last_digit if state else -last_digit
            state = not state
        return a_sum
