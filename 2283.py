# 2283. Check if Number Has Equal Digit Count and Digit Value
from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        d = defaultdict(lambda: 0)
        for n in num:
            d[int(n)] += 1

        for i, n in enumerate(num):
            if d[i] != int(n):
                return False

        return True


print(Solution().digitCount('1210'))
print(Solution().digitCount('030'))