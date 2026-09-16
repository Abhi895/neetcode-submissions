class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        if n <= 3:
            return n
        for i in range(2,n):
            n1, n2 = n2, n1 + n2
        return n2



        