""" probelm 234. Palindrome Linked List """


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
