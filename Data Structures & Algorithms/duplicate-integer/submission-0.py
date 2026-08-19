class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Maintain a hashmap to count instances.
        Counter = {}
        for num in nums:
            if num not in Counter.keys():
                Counter[num] = 1
            else:
                Counter[num] += 1
                return True
        return False
         