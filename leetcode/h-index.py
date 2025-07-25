class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        print(citations)
        for i, citation in enumerate(citations):
            if citation >= n - i:
                return n - i
        return 0