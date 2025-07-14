class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        c = 0
        left = ans = 0
        for right in range(len(s)):
            if right > 0 and s[right] == s[right-1]:
                c += 1
            while c > 1:
                if s[left] == s[left+1]:
                    c -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans