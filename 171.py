class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for char in columnTitle:
            char_val = ord(char.lower()) - ord("a") + 1
            total = total * 26 + char_val
        return total
