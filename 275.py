from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        citation_count = [0] * (length + 1)
        count = 0
        for i in range(length):
            if citations[i] >= length:
                citation_count[-1] += 1
            else:
                citation_count[citations[i]] += 1

        for i in range(length, -1, -1):
            count += citation_count[i]
            if count >= i:
                return i
