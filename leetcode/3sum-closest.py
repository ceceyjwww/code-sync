class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = inf
        
        n = len(nums)
        
        for i in range(n-2):
            x = nums[i]
            j = i + 1
            k = n - 1
            if i > 0 and x == nums[i-1]:
                continue

            if x + nums[i+1] + nums[i+2] > target:
                if abs(x + nums[i+1] + nums[i+2] - target) < min_diff:
                    min_diff = abs(x + nums[i+1] + nums[i+2] - target)
                    return x + nums[i+1] + nums[i+2]
                    
            if x + nums[-2] + nums[-1] < target:
                if abs(x + nums[-2] + nums[-1] - target) < min_diff:
                    min_diff = abs(x + nums[-2] + nums[-1] - target)
                    ans = x + nums[-2] + nums[-1]
                    continue
            
            while j < k:
                s = x + nums[j] + nums[k]
                diff = abs(s - target)
                if s < target:
                    if diff < min_diff:
                        min_diff = diff
                        ans = s
                    j += 1
                elif s > target:
                    if diff < min_diff:
                        min_diff = diff
                        ans = s
                    k -= 1
                else:
                    return s
        return ans