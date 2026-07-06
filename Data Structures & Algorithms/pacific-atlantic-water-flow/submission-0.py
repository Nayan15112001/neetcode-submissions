class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac,atl = set(),set()

        def dfs(r,c,seen,prev):
            #base condition
            if r<0 or c<0 or r>=n or c>=m or (r,c) in seen or heights[r][c]<prev:
                return

            seen.add((r,c))
            dfs(r+1,c,seen,heights[r][c])
            dfs(r-1,c,seen,heights[r][c])
            dfs(r,c-1,seen,heights[r][c])
            dfs(r,c+1,seen,heights[r][c])

        for col in range(m):
            dfs(0,col,pac,heights[0][col])
            dfs(n-1,col,atl,heights[n-1][col])

        for row in range(n):
            dfs(row,0,pac,heights[row][0])
            dfs(row,m-1,atl,heights[row][m-1])

        res = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pac and(r,c) in atl:
                    res.append([r,c])

        return res

