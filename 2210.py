# 6027. Count Hills and Valleys in an Array
# https://leetcode.com/contest/weekly-contest-285/problems/count-hills-and-valleys-in-an-array/


from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [nums[0]] + [nums[i] for i in range(1, N) if nums[i - 1] != nums[i]]

        N = len(nums)
        cnt = 0
        for i in range(1, N - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                cnt += 1
            elif nums[i - 1] > nums[i] and nums[i + 1] > nums[i]:
                cnt += 1
        return cnt


print(Solution().countHillValley([2, 4, 1, 1, 6, 5]))
print(Solution().countHillValley([6, 6, 5, 5, 4, 1]))
print(Solution().countHillValley([1, 2, 1, 2, 1]))