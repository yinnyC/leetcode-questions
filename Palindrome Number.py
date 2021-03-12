""" Problem 9. Palindrome Number"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Output: return True or Flase
        Edge case:
            if x is nagative: returen Flase
            if len(x) == 1 return True
        2 cases 
        1) len(x) is odd
         '12' 3 '21'  mid = (len(x)+1/2) -1
         left = x[:mid]
         right = x[mid+1:]
        --------------
        2) len(x) is even -> mid =len(x)/2
        right[:mid]
        left[mid:]
        10 01

        -> return left == right[::-1]
        """
        if x < 0:
            return False
        x = str(x)
        length = len(x)

        if length == 1:
            return True

        left, right = [], []
        if length % 2 != 0:  # odd
            mid = int((length+1)/2) - 1
            left = x[:mid]
            right = x[mid+1:]
        else:  # even
            mid = int(length/2)
            right = x[:mid]
            left = x[mid:]
        return left == right[::-1]
