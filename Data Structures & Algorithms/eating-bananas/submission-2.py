from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        def canFinish(rate: int) -> bool:
            hr_taken = 0
            for p in piles:
                hr_taken += ceil(p / rate)
            return hr_taken <= h

        while l < r:
            m = l + (r - l) // 2
            if canFinish(m):
                r = m
            else:
                l = m + 1

        return l