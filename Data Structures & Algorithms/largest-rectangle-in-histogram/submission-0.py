class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            right = i + 1
            while right < n and heights[right] >= height:
                right += 1

            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            right -= 1
            left += 1
            max_area = max(max_area, height * (right - left + 1))
        return max_area