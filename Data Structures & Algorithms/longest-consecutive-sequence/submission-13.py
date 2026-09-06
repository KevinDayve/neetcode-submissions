class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elements = set(nums)
        longest = 1
        for num in nums:
            if num+1 in elements:
                continue
            else:
                current = 1
                while num - 1 in elements:
                    current += 1
                    longest = max(current, longest)
                    num -= 1
        return longest
