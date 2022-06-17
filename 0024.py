# https://leetcode.com/problems/swap-nodes-in-pairs/
# 24. Swap Nodes in Pairs
from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(array: List[int]) -> ListNode:
    nodes = [ListNode(v) for v in array]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0] if len(nodes) > 0 else None


def print_list(node: ListNode):
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    print(ans)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        pre, cur = None, head

        while cur and cur.next:
            nex = cur.next
            cur.next, nex.next = nex.next, cur
            if pre:
                pre.next = nex
            pre, cur = cur, cur.next
        return new_head


print_list(Solution().swapPairs(create_list([1, 2, 3, 4])))
print_list(Solution().swapPairs(create_list([1, 2, 3, 4, 5])))
print_list(Solution().swapPairs(create_list([])))
print_list(Solution().swapPairs(create_list([1])))