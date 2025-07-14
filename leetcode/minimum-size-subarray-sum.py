class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = s = 0
        ans = n + 1

        for right, val in enumerate(nums):
            s += val
            while s >= target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left += 1
        return ans if ans <=n else 0