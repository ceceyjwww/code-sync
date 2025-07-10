class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left = ans = 0
        right = n - 1
        currA = capacityA
        currB = capacityB
        while left < right:
            if currB < plants[right]:
                currB = capacityB
                ans += 1
            currB -= plants[right]
            right -= 1
            if currA < plants[left]:
                currA = capacityA
                ans += 1
            currA -= plants[left]
            left += 1
        if left == right and max(currA, currB) < plants[left]:
            ans += 1
        return ans