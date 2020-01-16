import threading

# LeetCode: 1114. Print in Order
#
# This solution is from the dicsussion section:
# https://leetcode.com/problems/print-in-order/discuss/394392/Python-3-or-56ms-or-Lock-vs-Event
# It uses threading events.  The post also has a solution using locks.
# I'm just coding it out here to gain familiarity with multi-threading
# in Python

class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.event1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.event2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        