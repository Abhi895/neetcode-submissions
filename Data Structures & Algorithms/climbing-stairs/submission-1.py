class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        if n <= 3:
            return n
        for i in range(2,n):
            steps.append(steps[i-2] + steps[i-1])
        return steps[-1]

# (1,1), (2,2) (3,3) (4,5) (5,8) (6,13) (7.21)


        