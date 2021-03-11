# problem 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abc abc b b
        b b b b b
        pw wke w
        edge case - if is empty strig return 0
        """
        substring = ""
        ans = 0
        if len(s) != 0:
            for char in s:
                if char not in substring:
                    substring += char
                    ans = max(ans, len(substring))
                else:
                    cut = substring.index(char)
                    substring = substring[cut+1:] + char
        return ans
