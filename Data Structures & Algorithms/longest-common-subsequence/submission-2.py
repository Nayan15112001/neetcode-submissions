class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = {}
        ans = 0
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i>=n1 or j>=n2:
                return 0
            
            if text1[i] == text2[j]:
                dp[(i,j)] = 1+dfs(i+1,j+1)
            else:
                dp[(i,j)] = max(dfs(i,j+1), dfs(i+1,j))
            
            return dp[(i,j)]

        
        
        return dfs(0,0)