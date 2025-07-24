class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1] * n
        st = []
        idx = {x: i for i, x in enumerate(nums1)}
        for x in nums2:
            while st and x > st[-1]:
                ans[idx[st.pop()]] = x
            if x in nums1:
                st.append(x)
        return ans