# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
# 2380. Time Needed to Rearrange a Binary String
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        cnt = 0
        while '01' in s:
            s = s.replace('01', '10')
            cnt += 1
        return cnt


print(Solution().secondsToRemoveOccurrences('0110101'))
print(Solution().secondsToRemoveOccurrences('11100'))
print(Solution().secondsToRemoveOccurrences('001011'))