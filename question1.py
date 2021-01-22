# def twoSum(nums, target):
#     """
#      nums = [2,7,11,15], target = 9
#              ^
#                num2 = target - num1
#     """
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] == target:
#                 return [i, j]

def twoSum(nums, target):
    """
     nums = [2,7,11,15], target = 9
             ^
               num2 = target - num1
    """
    for i in range(len(nums)-1):
        num1 = nums[i]
        num2 = target-num1
        num2_pool = nums[i+1:]
        if num2 in num2_pool:
            return [i, (num2_pool).index(num2)+1+i]


print(twoSum([2, 7, 11, 15], 9))
