class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for a in range(n-3):
            if a and nums[a] == nums[a-1]:
                continue
            if nums[a] + nums[a+1] + nums[a+2] + nums[a+3] > target:
                break
            if nums[a] + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            for b in range(a+1, n-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                if nums[a] + nums[b] + nums[b+1] + nums[b+2] > target:
                    break
                if nums[a] + nums[b] + nums[-2] + nums[-1] < target:
                    continue

                c = b + 1
                d = n - 1
                
                while c < d:
                    x = nums[a] + nums[b] + nums[c] + nums[d]
                    if x == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif x > target:
                        d -= 1
                    else:
                        c += 1
        return ans