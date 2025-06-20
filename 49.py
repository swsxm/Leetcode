from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for word in strs:
            # convert word to tuple representation
            # ([a] - [z])
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            lookup[tuple(count)].append(word)
        return list(lookup.values())
