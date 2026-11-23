class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]

        right = [1] * len(nums)
        for j in range(1, len(nums)):
            right[len(nums)-j-1] = nums[len(nums)-j] *  right[len(nums)-j]
        return [l * r for (l,r) in zip(left, right)]

            
            