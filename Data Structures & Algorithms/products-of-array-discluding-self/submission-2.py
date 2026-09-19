class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 1, 2, 8]
        [48, 24, 6, 1]
        """
        n = len(nums)
        preprod = [1] * n
        postprod = [1] * n
        ans = [0] * n

        for i in range(1, n):
            preprod[i] = preprod[i - 1] * nums[i - 1]
            
        for i in range(n - 2, -1, -1):
            postprod[i] = postprod[i + 1] * nums[i + 1]
        
        for i in range(n):
            ans[i] = preprod[i] * postprod[i]
        
        return ans
        