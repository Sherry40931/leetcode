# https://leetcode.com/problems/smallest-number-in-infinite-set/
# 2336. Smallest Number in Infinite Set
import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self._heap = []
        self._set = set()
        self.cur = 1

    def popSmallest(self) -> int:
        if self._heap:
            num = heapq.heappop(self._heap)
            self._set.remove(num)
            return num
        self.cur += 1
        return self.cur - 1

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self._set:
            heapq.heappush(self._heap, num)
            self._set.add(num)


obj = SmallestInfiniteSet()
print(obj.addBack(2))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.addBack(1))
print(obj.addBack(1))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())