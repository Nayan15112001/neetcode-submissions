from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q= deque()
        ans = 0
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1

        if fresh == 0:
            return 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            size = len(q)
            rotted = False

            for _ in range(size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if nr<0 or nc<0 or nr>=n or nc>=m or grid[nr][nc]!=1:
                        continue
                    
                    grid[nr][nc] = 2
                    rotted = True
                    q.append((nr,nc))
                    fresh-=1
            if rotted:
                ans+=1
            

        if fresh>0:
            return -1

        return ans


