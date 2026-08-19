import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)):
            Product = int(math.prod(nums[:i] + nums[i+1:]))
            newList.append(Product)
        return newList