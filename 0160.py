from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(array: List[int]) -> Optional[ListNode]:
    head = node = ListNode(array[0])
    for a in array[1:]:
        next_node = ListNode(a)
        node.next = next_node
        node = next_node
    return head


def print_list(head: Optional[ListNode]):
    node = head
    while node:
        print(id(node) % 1000, node.val)
        node = node.next


class Solution:
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
    # time: O(m + n) * 2, space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i, j = headA, headB
        while i != j:
            # 如果 A, B 長度不同，i, j 會指到不同的 node
            # 所以最多會跑兩次，第二次 i, j 交換 list，長度就會一樣了：m + n == n + m
            i = i.next if i else headB
            j = j.next if j else headA
        return i


class Solution2:
    # time: O(m + n), space: O(m)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pool = set()

        # get nodes in list A
        node = headA
        while node:
            pool.add(node)
            node = node.next

        # check if nodes in list B is in pool
        node = headB
        while node:
            if node in pool:
                return node
            node = node.next
        return None


a = create_list([4, 1, 8, 4, 5])
b = create_list([5, 6, 1, 8, 4, 5])
a.next.next = b.next.next.next
print(Solution2().getIntersectionNode(a, b).val)

a = create_list([1, 9, 1, 2, 4])
b = create_list([3, 2, 4])
a.next.next.next = b.next
print(Solution2().getIntersectionNode(a, b).val)

a = create_list([1, 9, 1, 2, 4])
b = create_list([3, 2, 4])
print(Solution2().getIntersectionNode(a, b))