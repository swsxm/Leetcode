class Solution:
    def partitionString(self, s: str) -> int:
        lookup = [False] * 26
        result = 0
        base = ord("a")
        for char in s:
            pos = ord(char) - base
            if not lookup[pos]:
                lookup[pos] = True
            else:
                result += 1
                lookup = [False] * 26
                lookup[pos] = True
        return result + 1


Test = Solution()
print(Test.partitionString("abacaba"))
