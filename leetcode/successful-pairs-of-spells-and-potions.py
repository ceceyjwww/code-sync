class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        ans = [0] * len(spells)

        for i, val in enumerate(spells):
            left = -1
            right = n
            while left + 1 < right:
                mid = (left + right) // 2
                if potions[mid] * val < success:
                    left = mid
                else:
                    right = mid
            ans[i] = n - right
        return ans