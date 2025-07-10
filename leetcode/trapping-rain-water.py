class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = ans = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        while left <= right:
            suf_max = max(height[right], suf_max)
            pre_max = max(height[left], pre_max)
            if suf_max > pre_max:
                ans += (pre_max - height[left])
                left += 1
            else:
                ans += (suf_max - height[right])
                right -= 1
        return ans