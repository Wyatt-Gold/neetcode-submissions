# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        if size == n:
            temp = head.next
            head.next = None
            return temp
        
        position = size - n
        curr, prev = head, None
        while position > 0:
            prev = curr
            curr = curr.next
            position -= 1

        if not curr:
            temp = head.next
            head.next = None
            return temp
        
        prev.next = curr.next
        curr.next = None
        
        return head
