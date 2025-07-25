class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        return nums[(right-left)//2]