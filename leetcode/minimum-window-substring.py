class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, val in enumerate(s):
            cnt_s[val] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_right, ans_left = right, left
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right+1]