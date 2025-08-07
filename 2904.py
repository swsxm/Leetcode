class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, r = 0, 0
        substr = ""
        count = 0
        while r < len(s):
            if s[r] == "1":
                count += 1
            while l < r and count > k:
                if s[l] == "1":
                    count -= 1
                l += 1
            if count == k:
                # lets strip the string
                while s[l] == "0":
                    l += 1

                candidate = s[l : r + 1]
                if substr == "":
                    substr = candidate
                elif len(substr) > len(candidate):
                    substr = candidate
                elif len(substr) == len(candidate):
                    substr = substr if substr < candidate else candidate
            r += 1

        return substr
