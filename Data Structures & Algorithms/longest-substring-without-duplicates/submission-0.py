class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        Observed = {}
        left = 0
        for i, char in enumerate(s):
            if char in Observed and Observed[char] >= left:
                left = Observed[char] + 1
                # print(f'Our new left: {left}')
            Observed[char] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen