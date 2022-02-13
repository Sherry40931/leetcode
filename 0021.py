from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        output = []
        while self.next:
            output.append(str(self.val))
            self = self.next
        output.append(str(self.val))
        return ', '.join(output)


def create_list(array):
    if len(array) == 0:
        return []
    nodes = [ListNode(a) for a in array]
    for i in range(len(nodes[:-1])):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode(-1)  # dummy
        head = merge
        while list1 and list2:
            if list1.val < list2.val:
                merge, list1 = self.update(merge, list1)
            else:
                merge, list2 = self.update(merge, list2)

        merge.next = list1 or list2
        return head.next

    def update(self, merge: ListNode, node: ListNode):
        merge.next = node
        return merge.next, node.next


a, b = create_list([1, 2, 4]), create_list([1, 3, 4])
print(Solution().mergeTwoLists(a, b))
a, b = create_list([]), create_list([])
print(Solution().mergeTwoLists(a, b))
a, b = create_list([]), create_list([0])
print(Solution().mergeTwoLists(a, b))