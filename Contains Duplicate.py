""" Problem 217. Contains Duplicate """
def containsDuplicate(self, nums):
  """
  if len(set(nums)) < len(nums) return True
  """
  return True if len(set(nums)) < len(nums) else False 