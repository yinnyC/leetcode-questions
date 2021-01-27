""" problem 206. Reverse Linked List"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        edge case: 1. head = None
        """
        if head == None:
            return None
        new_head = ListNode(head.val)
        cur = head.next
        while cur:
            node_to_insert = ListNode(cur.val)
            node_to_insert.next = new_head
            new_head = node_to_insert
            cur = cur.next
        return new_head
            