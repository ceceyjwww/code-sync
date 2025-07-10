class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        n = len(height)
        right = n - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(area, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans