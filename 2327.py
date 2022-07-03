# https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# 2327. Number of People Aware of a Secret
class Solution:
    # https://leetcode.com/problems/number-of-people-aware-of-a-secret/discuss/2229982/JavaC%2B%2BPython-Sliding-window-O(n)-Time-O(forget)-Space
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        new = [1] + [0] * (n - 1)  # dp, #people who found secret on i-th day
        share = 0

        for day in range(1, n):
            add = new[day - delay] if day - delay >= 0 else 0  # people who can share today
            drop = new[day - forget] if day - forget >= 0 else 0  # people who forget today
            # new people = now who can share + new people who start sharing today - people who forget today
            new[day] = share + add - drop
            share = new[day]  # update people who can share after today
        return sum(new[-forget:]) % (10 ** 9 + 7)


print(Solution().peopleAwareOfSecret(6, 2, 4))  # 5
print(Solution().peopleAwareOfSecret(4, 1, 3))  # 6
print(Solution().peopleAwareOfSecret(6, 1, 2))  # 2