from collections import defaultdict


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        lookup = defaultdict(int)  # or use list
        for i in range(len(word1)):
            lookup[word1[i]] += 1
            lookup[word2[i]] -= 1
        for key in lookup:
            print(lookup[key])
            if abs(lookup[key]) > 3:
                return False
        return True


Test = Solution()
print(Test.checkAlmostEquivalent("zzzyyy", "iiiiii"))
