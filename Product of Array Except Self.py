""" Problem 238. Product of Array Except Self """


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 | 2*3*4, -> 1*24
        1 | *3*4,  -> 1*12
        1*2 | *4,  -> 2*4
        1*2*3 |1   -> 6*1
        left_arr * right_arr
        """
        length = len(nums)
        left_arr, right_arr, answer = [0] * length, [0] * length, [0] * length

        left_arr[0] = 1
        right_arr[length-1] = 1
        for i in range(1, length):
            left_arr[i] = left_arr[i-1] * nums[i-1]
        for i in reversed(range(len(nums) - 1)):
            right_arr[i] = right_arr[i+1] * nums[i+1]
        for i in range(length):
            answer[i] = left_arr[i]*right_arr[i]

        return answer
        # sol 2 O(N) ----> cannot get right answer when there is 0 in the list and notes says no devision
        """
        [1,2,3,4]
        product of all = 1*2*3*4 = 24
        answer = [24/1,24/2,24/3,24/4]
        edge case -> if num == 0 -> append(0)
        
        answer = []
        product_of_all = 1
        for num in nums:
            product_of_all *= num
        
        for i in range(len(nums)):
            if nums[i] != 0:
                answer.append(int(product_of_all/nums[i]))
            else:
                answer.append(product_of_all)
            
        return answer
        """
        # sol 1 brute force O(N**2)
        """
        answer = []
        for i in range(len(nums)):
            product = 1
            except_self = nums.copy()
            except_self.pop(i)
            for num in except_self:
                product *= num
            answer.append(product)
        return answer
        """
