# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers
from typing import List


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(array: List[int]) -> ListNode:
    nodes = [ListNode(v) for v in array]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


def print_list(node: ListNode):
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    print(ans)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        c = 0
        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            s = a + b + c
            if a + b + c >= 10:
                c = 1
                s -= 10
            else:
                c = 0
            ans.append(ListNode(s))
        if c > 0:
            ans.append(ListNode(c))

        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
        return ans[0]


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)  # not use
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            cur.next = ListNode(c % 10)
            cur = cur.next
            c //= 10

        return dummy.next  # bcuz line 58


print_list(Solution2().addTwoNumbers(create_list([2, 4, 3]), create_list([5, 6, 4])))
print_list(Solution2().addTwoNumbers(create_list([0]), create_list([0])))
print_list(Solution2().addTwoNumbers(create_list([9, 9, 9, 9, 9, 9, 9]), create_list([9, 9, 9, 9])))