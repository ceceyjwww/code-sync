class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        for i, val in enumerate(nums):
            r = bisect_right(nums, upper - val, 0, i)
            l = bisect_left(nums, lower - val, 0, i)
            ans += r - l
        return ans