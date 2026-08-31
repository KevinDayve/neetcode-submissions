class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            # The contained water is constrained by the smaller height:
            h = min(heights[left], heights[right])
            mostArea = max(mostArea, h * (right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mostArea