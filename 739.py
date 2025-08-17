from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        prev_temps = []
        for i in range(len(temperatures)):
            while prev_temps and temperatures[prev_temps[-1]] < temperatures[i]:
                idx = prev_temps.pop()
                result[idx] = i - idx
            prev_temps.append(i)
        return result
