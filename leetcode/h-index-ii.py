class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = len(citations) + 1

        while left + 1 < right:
            mid = (left + right) // 2
            if citations[-mid] >= mid:
                left = mid
            else:
                right = mid
        return left