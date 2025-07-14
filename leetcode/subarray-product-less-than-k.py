class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1:
            return 0
        left = 0
        s = 1
        ans = 0
        for right, val in enumerate(nums):
            s *= val
            while s >= k:
                s /= nums[left]
                left += 1
            ans += right - left + 1
        return ans