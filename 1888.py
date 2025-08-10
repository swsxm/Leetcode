class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        min_flips = n
        s = s + s
        p1 = [num % 2 for num in range(0, 2 * n)]
        p2 = [num % 2 for num in range(1, 2 * n + 1)]
        diff1 = sum(1 for i in range(n) if p1[i] != int(s[i]))
        diff2 = sum(1 for i in range(n) if p2[i] != int(s[i]))
        min_flips = min(diff1, diff2)
        for i in range(1, n):
            l = i - 1
            r = i - 1 + n

            if int(s[l]) != p1[l]:
                diff1 -= 1
            if int(s[r]) != p1[r]:
                diff1 += 1

            if int(s[l]) != p2[l]:
                diff2 -= 1
            if int(s[r]) != p2[r]:
                diff2 += 1

            min_flips = min(min_flips, diff2)
            min_flips = min(min_flips, diff1)

        return min_flips
