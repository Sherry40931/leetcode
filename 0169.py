# 169. Majority Element
# https://leetcode.com/problems/majority-element/
from typing import List
from timer import timing

from collections import defaultdict
from collections import Counter


class Solution:
    @timing
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(lambda: 0)
        half = len(nums) // 2
        for n in nums:
            cnt[n] += 1
            if cnt[n] > half:
                return n
        return max(cnt.values(), key=cnt.keys())

    @timing
    def majorityElement2(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement([1] * 10 ** 5 + [2] * 10 ** 3))
print(Solution().majorityElement2([3, 2, 3]))
print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement2([1] * 10 ** 5 + [2] * 10 ** 3))