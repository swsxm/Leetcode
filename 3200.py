class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def maxHeight(start, second):
            i = 1
            height = 0
            while start >= 0 and second >= 0:
                if i % 2 == 0:
                    start -= i
                else:
                    second -= i
                if start < 0 or second < 0:
                    return height
                height += 1
                i += 1
            return height

        return max(maxHeight(red, blue), maxHeight(blue, red))
