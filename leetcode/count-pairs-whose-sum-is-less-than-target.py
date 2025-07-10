class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        n = len(nums)
        right = n -1
        ans = 0
        while left < right:
            x = nums[left] + nums[right]
            if x < target:
                ans += (right-left)
                left += 1
            else:  #x >= target
                right -= 1
        return ans