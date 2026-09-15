from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_cnt = [(-cnt, num) for num, cnt in Counter(nums).items()]
        heapify(nums_cnt)
        ans = []
        while k > 0:
            curr = heappop(nums_cnt)
            ans.append(curr[1])
            k -= 1
        return ans 
        