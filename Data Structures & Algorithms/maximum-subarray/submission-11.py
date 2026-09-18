class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            if total >= 0:
                total += nums[i] 
            else:
                total = nums[i]
            if total > best:
                best = total
        return best
        