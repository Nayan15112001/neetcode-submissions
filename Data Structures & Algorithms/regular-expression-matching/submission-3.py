class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # . = anythin
        # * prev char * anything

        n1 = len(s)
        n2 = len(p)

        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if j==n2:
                return i==n1

            dp[(i,j)] = False

            match= i<n1 and (s[i] == p[j] or p[j] == '.')
            
            if j<n2-1 and p[j+1] == '*':
                dp[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))

            elif match:
                dp[(i,j)] = dfs(i+1,j+1)
            
            
            return dp[(i,j)]

        return dfs(0,0)

        

        