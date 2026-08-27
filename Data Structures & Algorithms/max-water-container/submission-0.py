class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mostArea = 0
        while left < right:
            height = min(heights[left], heights[right])
            mostArea = max(mostArea, height * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mostArea