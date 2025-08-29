from collections import defaultdict


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        k = k // 2
        lookup = defaultdict(int)
        for i in range(0, len(s), k):
            lookup[s[i : i + k]] += 1
            lookup[t[i : i + k]] += -1
        return all(val == 0 for val in lookup.values())
