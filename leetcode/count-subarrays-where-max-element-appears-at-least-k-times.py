class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = ans = count = 0
        max_element = max(nums)
        n = len(nums)
        if k > n:
            return 0

        for right, x in enumerate(nums):
            if x == max_element:
                count += 1
            while count >= k:
                if nums[left] == max_element:
                    count -= 1
                left += 1
            ans += left 
            
        return ans