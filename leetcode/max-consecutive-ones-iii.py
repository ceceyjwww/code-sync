class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        cnt = 0
        n = len(nums)

        for right, val in enumerate(nums):
            cnt += 1 - val
            while cnt > k:
                cnt -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans