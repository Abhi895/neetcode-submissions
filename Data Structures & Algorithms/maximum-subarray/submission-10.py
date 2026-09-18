class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max = nums[0]
        for i in range(1, len(nums)):
            if total >= 0:
                total += nums[i] 
            else:
                start = i
                total = nums[i]
            if total > max:
                max = total
        return max
        