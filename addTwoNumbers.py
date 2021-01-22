"""Problems 2. Add Two Numbers"""

def addTwoNumbers(l1, l2)
    ret = cur = ListNode(0)
    takeAway = 0
    while l1 or l2 or takeAway:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        
        total = v1 + v2 + takeAway
        takeAway = total//10
        val = total%10
        cur.next = ListNode(val)
        cur = cur.next 
        
    return ret.next