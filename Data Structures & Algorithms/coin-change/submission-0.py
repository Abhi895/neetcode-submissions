class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = [9999] * (amount+1)
        nums[0] = 0
        for i in range(1, amount+1):
            minC = 9999
            for c in coins:
                if i - c >= 0 and nums[i-c] != -1:
                    if nums[i-c] + 1 < minC:
                        minC = nums[i-c] + 1
            if minC == 9999:
                nums[i] = -1
            else:
                nums[i] = minC
        
        return nums[-1]

                    
        