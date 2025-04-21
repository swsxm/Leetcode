class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        o, a = ord, ord("a")
        for a1, a2 in zip(s, t):
            cnt[o(a1) - a] += 1
            cnt[o(a2) - a] -= 1

        return all(v == 0 for v in cnt)
