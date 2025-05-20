import random


class RandomizedSet:
    def __init__(self):
        self.lookup = dict()  # index: val
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        else:
            self.arr.append(val)
            self.lookup[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.lookup:
            index = self.lookup[val]
            last_val = self.arr[-1]
            self.arr[index] = last_val
            self.lookup[last_val] = index
            self.arr.pop()
            del self.lookup[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_num = random.randint(0, len(self.arr) - 1)
        return self.arr[random_num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
