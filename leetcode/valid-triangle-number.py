class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in range(n-1, 1, -1):
            j = 0
            k = i - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += (k - j)
                    k -= 1
                else:
                    j += 1
        return ans