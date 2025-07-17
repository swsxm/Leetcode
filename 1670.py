from typing import Optional


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class FrontMiddleBackQueue:
    def __init__(self):
        self.start: Optional[Node] = None
        self.middle: Optional[Node] = None
        self.size: int = 0
        self.end: Optional[Node] = None

    def pushFront(self, val: int) -> None:
        new_node = Node(val)
        if self.start:
            self.start.prev = new_node
            new_node.next = self.start
            self.start = new_node
            if self.size % 2 != 0:
                self.middle = self.middle.prev
        else:
            self.start = new_node
            self.middle = new_node
            self.end = new_node
        self.size += 1

    def pushMiddle(self, val: int) -> None:
        new_node = Node(val)
        if self.middle:
            if self.size % 2 == 0:
                tmp = self.middle.next
                self.middle.next = new_node
                new_node.prev = self.middle
                new_node.next = tmp
                tmp.prev = new_node
            else:
                if self.size != 1:
                    self.middle.prev.next = new_node
                else:
                    self.start = new_node
                new_node.prev = self.middle.prev
                new_node.next = self.middle
                self.middle.prev = new_node
        else:
            self.start = new_node
            self.end = new_node
        self.middle = new_node
        self.size += 1

    def pushBack(self, val: int) -> None:
        new_node = Node(val)
        if self.end:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node
            if self.size % 2 == 0:
                self.middle = self.middle.next
        else:
            self.start = new_node
            self.middle = new_node
            self.end = new_node
        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        value = self.start.val
        if self.size == 1:
            self.middle = None
            self.start = None
            self.end = None
            self.size -= 1
            return value
        self.start = self.start.next
        if self.start:
            self.start.prev = None
        if self.size % 2 == 0:
            self.middle = self.middle.next
        self.size -= 1
        return value

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1

        value = self.middle.val
        if self.size == 1:
            self.start = None
            self.middle = None
            self.end = None
            self.size -= 1
            return value
        if self.size == 2:
            return self.popFront()
        tmp = self.middle.prev
        if self.size % 2 == 0:
            self.middle.prev.next = self.middle.next
            self.middle.next.prev = tmp
            self.middle = self.middle.next
        else:
            self.middle.prev.next = self.middle.next
            self.middle.next.prev = tmp
            self.middle = self.middle.prev

        self.size -= 1
        return value

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        value = self.end.val
        if self.size == 1:
            self.start = None
            self.middle = None
            self.end = None
            self.size -= 1
            return value
        if self.end:
            self.end = self.end.prev
            self.next = None
        if self.size % 2 != 0:
            self.middle = self.middle.prev
        self.size -= 1
        return value


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
