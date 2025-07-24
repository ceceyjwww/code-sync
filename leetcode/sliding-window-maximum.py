class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, x in enumerate(nums):
            while q and x > nums[q[-1]]:
                q.pop()
            q.append(i)
            
            if i - q[0] >= k:
                q.popleft()
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans