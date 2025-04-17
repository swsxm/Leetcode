class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        is_word = False
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
                is_word = True
            elif is_word:
                return count
        return count
