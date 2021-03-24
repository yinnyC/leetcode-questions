""" Problem 1198. Find Smallest Common Element in All Rows """


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        all_rows = len(mat)
        common_elems = {}
        all_rows_common_elems = []
        for i in range(0, all_rows):
            for j in range(0, len(mat[i])):
                target = mat[i][j]
                if target in common_elems:
                    common_elems[target] += 1
                else:
                    common_elems[target] = 1
                if common_elems[target] == all_rows:
                    all_rows_common_elems.append(target)
        if len(all_rows_common_elems) == 0:
            return -1
        else:
            return all_rows_common_elems[0]
