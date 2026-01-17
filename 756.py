from typing import List
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        patterns = defaultdict(list)
        for pattern in allowed:
            patterns[pattern[:2]].append(pattern[2])

        lookup = {}
        def dfs(current_layer, next_layer):
            state = (current_layer, next_layer)
            if state in lookup:
                return lookup[(current_layer, next_layer)]

            if len(current_layer) == 1:
                return True
            if len(next_layer) == len(current_layer) - 1:
                return dfs(next_layer, "")

            left = current_layer[len(next_layer)] 
            right = current_layer[len(next_layer) + 1] 

            for option in patterns[left + right]:
                res = dfs(current_layer, next_layer + option)
                if res:
                    lookup[state] = True
                    return True

            lookup[state] = False
            return False
        return dfs(bottom, "")
