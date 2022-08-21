# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# 2379. Minimum Recolors to Get K Consecutive Black Blocks
class Solution:
    def minimumRecolors(self, bs: str, k: int) -> int:
        blocks = bs.replace('B', '1').replace('W', '0')
        cur_b = sum(int(v) for v in blocks[:k])
        min_w = k - cur_b
        n = len(blocks)
        for i in range(n - k):
            cur_b = cur_b - int(blocks[i]) + int(blocks[i + k])
            min_w = min(min_w, k - cur_b)
        return min_w


print(Solution().minimumRecolors('WBBWWBBWBW', 7))
print(Solution().minimumRecolors('WBWBBBW', 2))