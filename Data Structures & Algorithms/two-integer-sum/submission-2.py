class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialise a dict
        seen: dict = {}
        for index, number in enumerate(nums):
            # check if that number is already present in our dict
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            # otherwise just add that number to our seen map.
            seen[number] = index
        