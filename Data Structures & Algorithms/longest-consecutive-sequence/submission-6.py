class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        consec_dict = defaultdict(int) 

        for num in nums:
            consec_dict[num] = 1 + consec_dict[num - 1]
            
        return max(consec_dict.values())
