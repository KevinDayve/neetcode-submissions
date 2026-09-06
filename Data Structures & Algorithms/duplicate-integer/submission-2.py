class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i, num in enumerate(nums):
            if num not in counter:
                counter[num] = 1
            else:
                return True
        return False