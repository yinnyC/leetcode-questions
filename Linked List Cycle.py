""" Problem 141.  Linked List Cycle"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen_node = {}
        while head:
            if head in seen_node:
                return True
            seen_node[head]=head
            head = head.next
        return Falseå