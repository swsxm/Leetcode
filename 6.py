class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        levels = [""] * numRows

        level = 0
        increase = False
        for i in range(len(s)):
            if level == 0 or level == numRows - 1:
                increase = not increase
            levels[level] = levels[level] + s[i]
            level += 1 if increase else -1
        return "".join(levels)
