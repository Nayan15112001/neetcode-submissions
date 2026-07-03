class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n= len(grid)
        m= len(grid[0])
        self.seen= set()
        count=0
        
        def dfs(r,c):
            
            #base condition to break the recursion
            if r<0 or c<0 or r>=n or c>=m or (r,c) in self.seen or grid[r][c]!='1':
                return 
            
            self.seen.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)



        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in self.seen:
                    dfs(i,j)
                    count += 1
        

        return count