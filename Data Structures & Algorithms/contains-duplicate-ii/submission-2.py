class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i, num in enumerate(nums):
            if num in freq and i - freq[num] <= k:
                return True
            freq[num] = i
        return False