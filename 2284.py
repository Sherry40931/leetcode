# 2284. Sender With Largest Word Count
from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt = defaultdict(lambda: 0)
        for sender, msg in zip(senders, messages):
            cnt[sender] += len(msg.split())

        max_sender = senders[0]
        max_len = cnt[max_sender]
        for sender, length in cnt.items():
            if (length > max_len) or (length == max_len and sender > max_sender):
                max_len = length
                max_sender = sender

        return max_sender


print(Solution().largestWordCount(
    ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"],
    ["Alice", "userTwo", "userThree", "Alice"]))
print(Solution().largestWordCount(
    ["How is leetcode for everyone", "Leetcode is useful for practice"],
    ["Bob", "Charlie"]))