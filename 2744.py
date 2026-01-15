from typing import List
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0
        reversed_words = set()

        for word in words:
            if word in reversed_words:
                counter += 1
            else:
                reversed_words.add(word[::-1])
        return counter