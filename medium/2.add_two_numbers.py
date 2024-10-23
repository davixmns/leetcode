from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_list = ["", ""]

        while l1:
            str_list[0] = str(l1.val) + str_list[0]
            l1 = l1.next

        while l2:
            str_list[1] = str(l2.val) + str_list[1]
            l2 = l2.next

        number_sum = str(int(str_list[0]) + int(str_list[1]))
        number_list = [int(i) for i in number_sum]

        dummy = ListNode(0)
        current = dummy

        for n in reversed(number_list):
            current.next = ListNode(n)
            current = current.next

        return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(Solution().addTwoNumbers(l1, l2))