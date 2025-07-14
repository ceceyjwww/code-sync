class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        n = len(nums)
        c = Counter()
        for right, val in enumerate(nums):
            c[val] += 1
            while c[val] > k:
                c[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans