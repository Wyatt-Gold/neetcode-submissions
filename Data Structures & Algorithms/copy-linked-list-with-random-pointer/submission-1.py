"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        temp = head
        while head:
            new_node = Node(head.val)
            nodes[head] = new_node
            head = head.next
        head = temp
        
        new_head = nodes[head]
        while head:
            curr_node = nodes[head]
            next_node = nodes.get(head.next, None)
            random_node = nodes.get(head.random, None)
            curr_node.next = next_node
            curr_node.random = random_node
            head = head.next
        
        return new_head