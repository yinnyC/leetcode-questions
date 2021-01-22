# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1, l2):
        """
        1. traverse each node [2,4,3,1] [5,6,4]
        [2,4,3,1] -> [7,0,8,1] -> 
        [5,6,4,0] 
        """
        l1_nums, l2_nums = [], []
        while l1 and l2:
            l1_nums.append(l1.val if l1.val else 0)
            l2_nums.append(l2.val if l2.val else 0)
            l1 = l1.next
            l2 = l2.next
        result = []
        carry = 0
        for num1, num2 in zip(l1_nums, l2_nums):
            sum = num1+num2+carry
            carry = 0
            if sum > 9:
                sum %= 10
                carry = 1
            result.append(sum)
        sum = ListNode(0)
        for num in result[::-1]:
            sum.val = num
