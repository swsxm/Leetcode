class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        s = list(s)
        while i < len(s):
            remaining = min(k, len(s) - i)
            for j in range(remaining // 2):
                s[i + j], s[i + remaining - j - 1] = s[i + remaining - j - 1], s[i + j]
            i += 2 * k
        return "".join(s)
