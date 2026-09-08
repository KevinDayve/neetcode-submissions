class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        freq = {}
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while True:
                maxFreq = max(freq.values())
                currLen = right - left + 1
                if currLen - maxFreq <= k:
                    break
                freq[s[left]] -= 1
                left += 1
            length = max(length, (right - left + 1))
        return length
            