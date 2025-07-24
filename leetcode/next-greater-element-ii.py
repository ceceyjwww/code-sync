class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n):
            x = nums[i % n]
            while st and x > nums[st[-1]]:
                ans[st.pop()] = x
            if i < n:
                st.append(i)
        return ans