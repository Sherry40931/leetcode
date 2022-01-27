# 2144. Minimum Cost of Buying Candies With Discount
# 2022/01/23

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        cost.sort(reverse=True)
        ans, N = 0, len(cost)

        for i in range(0, N, 3):
            if i + 1 < N:
                ans += cost[i] + cost[i + 1]
            else:
                ans += cost[i]
        return ans