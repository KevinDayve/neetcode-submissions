class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        observed = set(nums)
        longest = 0
        for num in observed:
            if num - 1 not in observed:
                current_num = num
                consecutive = 1
                while current_num + 1 in observed:
                    consecutive += 1
                    current_num += 1
                longest = max(longest, consecutive)

        return longest