"""Problems 19. Remove Nth Node From End of List""" 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(self, head, n):
  """
        singly-linked-list
        1. traverse
        pointer point to cur.next 
        [1,2,3,4,5] n=2
               ^ ^    n=2 - find the cur while cur.next x1 is the last node   
             cur cur+n     n=3 - find the cur while cur.next x2 is the last node
             
        edge case: 
        1. only one node in the linked list 
        2. head node is the target to remove
        """
  def get_n_after_cur(cur,n):
            pointer = cur
            if n == 0:
                return pointer.next
            for _ in range(n-1):
                pointer = pointer.next
            return pointer            
        
        if head.next == None:
            # if there's only one node
            head = None
            return head

        cur = head
        prev = None
        n_after_cur = get_n_after_cur(cur,n)
        if n_after_cur.next == None: 
            # target to remove is the head node
            head = head.next
            return head
        while n_after_cur.next != None:
            prev = cur
            cur = cur.next
            n_after_cur = get_n_after_cur(cur,n)
        prev.next = cur.next
        return head

        