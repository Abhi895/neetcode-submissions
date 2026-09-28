class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
                needed = nums[i] + 1
                length = 1
                while needed in seen:
                    length += 1
                    needed += 1
                if length > maxLength:
                    maxLength = length
        
        return maxLength

        


    # -----------
    # BRUTE FORCE
    # ------------
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     nums.sort()
    #     maxLength = 0
    #     for i in range(len(nums)):
    #         curr = nums[i]
    #         length = 1
    #         for j in range(i+1, len(nums)):
    #             if nums[j] == (curr + 1):
    #                 length += 1
    #                 curr = nums[j]
    #         if length > maxLength:
    #             maxLength = length
    #     return maxLength

