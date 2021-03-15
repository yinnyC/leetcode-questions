"""349. Intersection of Two Arrays"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. find the shorter one
        2. Interate thru the list and if a element is in another list, append the element to the ans_list
        3. beofre we append. we check if the elem is in the ans_list, if Ture, don't append

        Edge case:
        1. one list is empty -> return empty []

        """
        ans = []
        if len(nums1) == 0 or len(nums2) == 0:
            return ans
        # assume len(nums1) < len(nums2)
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        for elem in nums1:
            if elem in nums2 and elem not in ans:
                ans.append(elem)

        return ans
