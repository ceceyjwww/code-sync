class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        n = len(prices)
        ans = prices
        for i, x in enumerate(prices):
            while st and x <= prices[st[-1]]:
                ans[st[-1]] = prices[st[-1]] - x
                st.pop()
            st.append(i)
        return ans