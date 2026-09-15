class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        mid = (len(nums)-1) // 2 
        r = len(nums) - 1
        i = 0
        while i <= len(nums):
            if target > nums[mid]:
                l = mid 
                mid = l + (r +1 - l) // 2 
            elif target < nums[mid]:
                r = mid 
                mid = l + (mid-1) // 2
            else:
                return mid
            i += 1
        return -1
        