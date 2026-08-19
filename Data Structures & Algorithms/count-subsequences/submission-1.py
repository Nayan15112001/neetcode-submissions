class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        i,j = 0,0
        n1,n2 = len(s),len(t)
        dp = {}

        if n1<n2:
            return 0

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if j == n2:
                return 1
            if i>=n1 or j>n2:
                return 0
            
            temp = 0
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            
            else:
                dp[(i,j)] = dfs(i+1,j)

            if (i,j) not in dp:
                dp[(i,j)] = temp
            
            return dp[(i,j)]
        
        return dfs(0,0)

        



