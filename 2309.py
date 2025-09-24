class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
        for i in range(26):
            letter = chr(ord("z") - i)
            if letter in chars and letter.upper() in chars:
                return letter.upper()
        return ""
