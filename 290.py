class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lookup = {}
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in lookup:
                if lookup[pattern[i]] != s_list[i]:
                    return False
            else:
                if s_list[i] in lookup.values():
                    return False
                lookup[pattern[i]] = s_list[i]
        return True
