class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for c in magazine:
            count[ord(c) - ord("a")] += 1
        for c in ransomNote:
            if count[ord(c) - ord("a")] == 0:
                return False
            else:
                count[ord(c) - ord("a")] -= 1
        return True
