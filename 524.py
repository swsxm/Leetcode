from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda w: (-len(w), w))
        for word in dictionary:
            i, j = 0, 0
            while i < len(s):
                if s[i] == word[j]:
                    j += 1
                i += 1
                if j == len(word):
                    return word
        return ""
