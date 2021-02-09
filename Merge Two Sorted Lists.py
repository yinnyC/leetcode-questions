""" Problems 21. Merge Two Sorted Lists"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        edge cases/ base case:
        1. empty linkedlist node
        -> Return the other linked list
        """
        ret = ListNode()
        cur = ret

        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val <= l2.val:
            cur.next = l1
            cur.next.next = self.mergeTwoLists(l1.next, l2)
        elif l2.val <= l1.val:
            cur.next = l2
            cur.next.next = self.mergeTwoLists(l1, l2.next)
        return ret.next
