from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0
        tank = 0
        start = 0
        for i in range(0, len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total_diff += diff
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_diff >= 0 else -1
