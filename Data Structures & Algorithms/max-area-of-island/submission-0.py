class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n = len(grid)
        m = len(grid[0])
        self.seen = set()


        def dfs(r,c):
            
            #base condition
            if r<0 or c<0 or r>=n or c>=m or (r,c) in self.seen or grid[r][c]==0:
                return 
            
            self.seen.add((r,c))
            self.island.append(grid[r][c])
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            
            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in self.seen:
                    self.island = []
                    dfs(i,j)
                    area = len(self.island)
                    print(self.island)
                    maxArea = max(area,maxArea)

        
        return maxArea
