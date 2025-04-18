class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return index

    def strStr2(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return index
