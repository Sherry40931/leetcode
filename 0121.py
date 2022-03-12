# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = prices[0], 0
        for p in prices[1:]:
            ans = max(ans, p - buy)
            buy = min(buy, p)
        return ans