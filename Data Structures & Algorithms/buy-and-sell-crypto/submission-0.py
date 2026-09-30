class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest_so_far = prices[0]
        n = len(prices)

        for i in range(1, n):
            ans = max(ans, prices[i] - lowest_so_far)
            lowest_so_far = min(lowest_so_far, prices[i])

        return ans 