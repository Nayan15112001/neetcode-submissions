class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = {}

        # def dfs(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     if i == m-1 and j == n-1:
        #         return 1

        #     if i<0 or i>=m or j<0 or j>=n:
        #         return 0

            
        #     dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1)

        #     return dp[(i,j)]
        
        # return dfs(0,0)

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                else:
                    if i+1<m:
                        dp[i][j] += dp[i+1][j]
                    if j+1<n:
                        dp[i][j] += dp[i][j+1]

        return dp[0][0]