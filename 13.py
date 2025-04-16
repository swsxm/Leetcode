class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        check = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        i = 0
        sum = 0
        while i < len(s):
            if s[i] in check and i + 1 < len(s) and s[i + 1] in check[s[i]]:
                sum += lookup[s[i + 1]] - lookup[s[i]]
                i += 2
            else:
                sum += lookup[s[i]]
                i += 1
        return sum

    def romanToInt2(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and lookup[s[i + 1]] > lookup[s[i]]:
                result -= lookup[s[i]]
            else:
                result += lookup[s[i]]
        return result
