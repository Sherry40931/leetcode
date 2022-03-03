from typing import List


class Solution:
    # cheat, use extra space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        result = [0] * (m + n)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result[i + j] = nums1[i]
                i += 1
            elif j < n:
                result[i + j] = nums2[j]
                j += 1
        if i < m:
            result[i + j:] = nums1[i:]
        elif j < n:
            result[i + j:] = nums2[j:]

        for i in range(m + n):
            nums1[i] = result[i]


class Solution2:
    # fill blank from the back
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]


a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
Solution2().merge(a, 3, b, 3)
print(a)

a = [1]
b = []
Solution2().merge(a, 1, b, 0)
print(a)

a = [0]
b = [1]
Solution2().merge(a, 0, b, 1)
print(a)