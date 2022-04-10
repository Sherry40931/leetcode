# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        ans = []
        for n in nums2:
            if n in set1:
                set1.remove(n)
                ans.append(n)
        return ans


print(Solution2().intersection([1, 2, 2, 1], [2, 2]))
print(Solution2().intersection([4, 9, 5], [9, 4, 9, 8, 4]))