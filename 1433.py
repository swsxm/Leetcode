class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        direction = 0  # 0 = undecided, 1 = s1 breaks s2, -1 = s2 breaks s1
        for c1, c2 in zip(s1, s2):
            if direction == 0:
                if c1 > c2:
                    direction = 1
                elif c1 < c2:
                    direction = -1
            elif direction == 1 and c1 < c2:
                return False
            elif direction == -1 and c1 > c2:
                return False
        return True
