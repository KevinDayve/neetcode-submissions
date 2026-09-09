class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLength = float("inf")

        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                # Update the minimum length:
                minLength = min(minLength, (right - left + 1))
                currSum -= nums[left]
                left += 1
        if minLength == float("inf"): return 0
        return minLength