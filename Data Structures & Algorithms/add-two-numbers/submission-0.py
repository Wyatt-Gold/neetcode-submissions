# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val + carry
            carry = digit // 10
            digit %= 10
            curr.val = digit
            l1 = l1.next
            l2 = l2.next
            if l1 or l2 or carry != 0:
                curr.next = ListNode()
                curr = curr.next
        
        while l1:
            digit = l1.val + carry
            carry = digit // 10
            digit %= 10
            curr.val = digit
            l1 = l1.next
            if l1 or carry != 0:
                curr.next = ListNode()
                curr = curr.next

        while l2:
            digit = l2.val + carry
            carry = digit // 10
            digit %= 10
            curr.val = digit
            l2 = l2.next
            if l2 or carry != 0:
                curr.next = ListNode()
                curr = curr.next
        
        if carry != 0:
            curr.val = carry

        return head