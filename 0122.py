# 122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = prices[0], 0
        for p in prices[1:]:
            ans += max(0, p - buy)
            if p - buy > 0:
                buy = p
            buy = min(buy, p)
        return ans


class Solution2:
    def maxProfit(self, p: List[int]) -> int:
        return sum([max(0, p[i] - p[i - 1]) for i in range(1, len(p))])