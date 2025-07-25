class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        border = 0
        step = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == border:
                step += 1
                border = furthest
        return step