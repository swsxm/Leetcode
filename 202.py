class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()
        while n not in lookup:
            lookup.add(n)
            # if no cast to string allowed
            # use divmod...
            n = sum(int(num) ** 2 for num in str(n))
            if n == 1:
                return True
        return False
