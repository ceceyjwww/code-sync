class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        left = 0
        ans = 0
        for right, val in enumerate(s):
            c[val] += 1
            while c[val] > 1:
                c[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans