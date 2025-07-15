class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        ans = -1
        k = sum(nums) - x
        if k < 0:
            return -1
        s = 0

        for right, val in enumerate(nums):
            s += val
            while s > k:
                s -= nums[left]
                left += 1
            if s == k:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans