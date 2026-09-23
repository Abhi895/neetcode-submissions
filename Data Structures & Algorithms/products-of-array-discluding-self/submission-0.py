class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        outputs = [0] * len(nums)
        zeroFound = False
        zeroInd = -1
        zeroesFound = False
        
        for (i, n) in enumerate(nums):
            if n != 0:
                product *= n
            elif not zeroFound:
                zeroFound = True
                zeroInd = i
            else:
                zeroesFound = True
        if zeroesFound:
            return outputs
        if zeroFound:
            outputs[zeroInd] = product
            return outputs

        for i in range(len(nums)):
            outputs[i] = product // nums[i]
        return outputs
        
        
        