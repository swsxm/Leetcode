from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        lookup = [-1] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord("a")
            if lookup[index] == -1:
                lookup[index] = i
            else:
                if i - lookup[index] - 1 != distance[index]:
                    return False
        return True
