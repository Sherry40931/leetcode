from typing import List


class Solution:
    # Kadane's Algorithm
    # O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        ans = s = nums[0]
        for n in nums[1:]:
            s = max(n, s + n)  # 目前最大 sum 都是由前一個最大 sum 得來 (dynamic programming)
            ans = max(ans, s)
        return ans


class Solution2:
    # divide and conquer
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        mid = N // 2
        if mid == 0:
            return nums[0]

        # merge
        s_max_l = s = nums[mid]
        for n in nums[mid - 1::-1]:
            s += n
            s_max_l = max(s_max_l, s)

        s_max_r = s = nums[mid]
        for n in nums[mid + 1:]:
            s += n
            s_max_r = max(s_max_r, s)

        return max(self.maxSubArray(nums[:mid]),
                   self.maxSubArray(nums[mid:]),
                   s_max_l + s_max_r - nums[mid])


print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution2().maxSubArray([1]))
print(Solution2().maxSubArray([5, 4, -1, 7, 8]))
print(Solution2().maxSubArray([-2, -1]))