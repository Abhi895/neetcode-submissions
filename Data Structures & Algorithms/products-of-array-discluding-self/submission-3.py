class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        zeroFound = -1
        for i in range(len(nums)):
            if nums[i] != 0 or zeroFound != -1:
                product *= nums[i] 
            else:
                zeroFound = i
        if zeroFound != -1:
            outputs = [0] * len(nums)
            outputs[zeroFound] = product
            return outputs
        else:
            return [product // n for n in nums]        

            
            