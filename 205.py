class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                if t[i] != hashmap[s[i]]:
                    return False
            else:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
        return True
