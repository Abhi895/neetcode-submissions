class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = set()

        def dfsFrom(r, c):
            if r < 0 or r >= m:
                return
            if c < 0 or c >= n:
                return
            if grid[r][c] == "0":
                return
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            dfsFrom(r+1, c)
            dfsFrom(r, c+1)
            dfsFrom(r-1, c)    
            dfsFrom(r, c-1)        
    
        for r in range(m):
            for c in range (n):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfsFrom(r, c)
                    count += 1
        
        return count