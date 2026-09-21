class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        minCosts = [0] * n

        for i in range(2, n):
            minCosts[i] = min(minCosts[i-1] + cost[i-1], minCosts[i-2] + cost[i-2])
        
        return minCosts[-1]