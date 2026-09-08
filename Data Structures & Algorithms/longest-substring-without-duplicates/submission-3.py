class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Implement a counter to keep track of things;
        counter = {}
        left = 0
        length = 0
        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]] = right # Track the index;
            elif s[right] in counter and counter[s[right]] >= left:
                left = counter[s[right]] + 1
            counter[s[right]] = right
            length = max(length, right-left+1)
        return length