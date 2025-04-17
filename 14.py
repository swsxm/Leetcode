from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[0][j] != strs[i][j]:
                    return strs[0][:j]
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        prefix_len = len(strs[0])

        for i in range(1, len(strs)):
            for j in range(prefix_len):
                if j > len(strs[i]) - 1 or strs[i][j] != strs[0][j]:
                    prefix_len = j
                    break
        return strs[0][:prefix_len]
