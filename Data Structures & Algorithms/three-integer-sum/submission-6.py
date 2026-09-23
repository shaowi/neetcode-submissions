class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        processed = set()
        n = len(nums)

        for i in range(n):
            j, k = i + 1, n - 1
            target = -nums[i]
            while j < k:
                two_sum = nums[j] + nums[k]
                comb = (nums[i], nums[j], nums[k])
                if two_sum == target and comb not in processed:
                    processed.add(comb)
                elif two_sum > target:
                    k -= 1
                else:
                    j += 1

        return [[comb[0], comb[1], comb[2]] for comb in processed]