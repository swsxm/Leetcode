class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_factor = minutes / 60
        hour_degree = ((hour + minute_factor) % 12) / 12 * 360
        minute_degree = minute_factor * 360
        diff = abs(minute_degree - hour_degree)
        return min(diff, 360 - diff)


Test = Solution()
print(Test.angleClock(hour=1, minutes=57))
