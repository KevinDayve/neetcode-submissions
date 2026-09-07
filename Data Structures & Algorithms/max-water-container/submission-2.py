class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We want to maximise the area;
        left = 0
        right = len(heights) - 1
        maximumArea = 0

        while left < right:
            h = min(heights[left], heights[right])
            maximumArea = max(maximumArea, h * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximumArea