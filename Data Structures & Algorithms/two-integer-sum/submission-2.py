class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        i = 0
        while i < len(nums):
            need[target-nums[i]] = i
            i += 1
            if nums[i] in need:
                return ([need[nums[i]], i])
            

        