# 2145. Count the Hidden Sequences
# 2022/01/23

class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        min_d, max_d = 0, 0
        s = 0
        for i, d in enumerate(diff):
            s += d
            min_d = min(min_d, s)
            max_d = max(max_d, s)

        ans = (upper - max_d) - (lower - min_d) + 1
        # print(ans, min_d, max_d)
        if ans < 0:
            ans = 0
        return ans
