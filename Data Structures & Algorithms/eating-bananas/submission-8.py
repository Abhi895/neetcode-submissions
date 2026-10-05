
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = (sum(piles) + h - 1) // h
        
        currK = minK
        currH = sum([(x + currK - 1) // currK for x in piles])

        l = minK
        r = max(piles)
        while l < r:
            m = (r + l) // 2
            currK = m
            newH = sum([(x + currK - 1) // currK for x in piles])
            if newH <= h:
                r = m
            else:
                l = m + 1

        return (l + r) // 2

