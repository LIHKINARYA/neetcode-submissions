class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        maxarea = min(heights[l],heights[r]) * (r - l)
        top = max(heights)


        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea