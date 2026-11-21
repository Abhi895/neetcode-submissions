class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxMoney = [nums[i] for i in range(n)]
        for i in range(1, n):
            if i == 1:
                maxMoney[1] = max(maxMoney[0], maxMoney[1])
            else:
                maxMoney[i] = max(maxMoney[i-2] + nums[i], maxMoney[i-1])

        return max(maxMoney) 


        

        