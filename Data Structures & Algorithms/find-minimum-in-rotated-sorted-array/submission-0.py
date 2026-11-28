class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self._findMin(nums, 0, len(nums) - 1)

    def _findMin(self, nums: List[int], l: int, r: int) -> int:
        """
        l: left
        m: mid
        r: right

        m < r : (l, m) 
        m >= r: (m + 1, r)
        """

        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
                
        return nums[l]            