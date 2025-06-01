class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        # or use dict and update always skip in between chars
        max_len = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            max_len = max(max_len, len(substr))
            r += 1
        return max_len


Test = Solution()
print(Test.lengthOfLongestSubstring("abcabcbb"))
