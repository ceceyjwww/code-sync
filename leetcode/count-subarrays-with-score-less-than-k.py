class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        summ = 0

        for right, x in enumerate(nums):
            summ += x
            while summ * (right - left + 1) >= k:
                summ -= nums[left]
                left += 1
            ans += right - left + 1
        return ans