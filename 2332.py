# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# 2332. The Latest Time to Catch a Bus
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        i, c, m = 0, 0, len(passengers)
        last = buses[0]

        for bus in buses:
            c = 0
            while i < m and passengers[i] <= bus and c < capacity:
                c, i = c + 1, i + 1

        last = bus if c < capacity else passengers[i - 1]
        booked = set(passengers)
        for time in range(last, 0, -1):
            if time not in booked:
                return time


print(Solution().latestTimeCatchTheBus([10, 20], [2, 17, 18, 19], 2))
print(Solution().latestTimeCatchTheBus([10, 17], [2, 17, 18, 19], 2))
print(Solution().latestTimeCatchTheBus([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2))