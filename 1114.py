import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.sem1 = threading.Semaphore(0)
        self.sem2 = threading.Semaphore(0)

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.

        printFirst()
        self.sem1.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.sem1.acquire()
        printSecond()
        self.sem2.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.sem2.acquire()
        printThird()
        self.sem2.release()
