class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = {}
        ans,temp = 0,0
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i>=n or j>=m or i<0 or j<0:
                return 0
            u,d,l,r = 0,0,0,0
            if i<n-1 and matrix[i+1][j]>matrix[i][j]:
                d = dfs(i+1,j)
            
            if i>0 and matrix[i-1][j]>matrix[i][j]:
                u = dfs(i-1,j)
            
            if j<m-1 and matrix[i][j+1]>matrix[i][j]:
                r = dfs(i,j+1)
            
            if j>0 and matrix[i][j-1]>matrix[i][j]:
                l = dfs(i,j-1)
            print(i,j)
            print(u,d,r,l)
            dp[(i,j)] = 1+max(u,d,r,l)

            return dp[(i,j)]
        
        for i in range(n):
            for j in range(m):
                temp = dfs(i,j)
                ans = max(ans,temp)
        
        return ans
