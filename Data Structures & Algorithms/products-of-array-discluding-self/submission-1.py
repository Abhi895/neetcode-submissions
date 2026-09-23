class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        outputs= [1] * len(nums)

        for i in range(1, len(nums)):
            product *= nums[i-1]
            outputs[i] = product
        
        product = 1
        for i in range(len(nums)):
            outputs[len(nums)-i-1] *= product
            product *= nums[len(nums)-i-1]


        return outputs
        
        