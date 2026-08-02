class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
        best_left,best_right,max_len,length = 0,0,1,1
        for l in range(n-1,-1,-1):
            for r in range(l+1,n):
                if r-l+1<=2:
                    dp[l][r] = (s[l] == s[r])
                    
                else:
                    dp[l][r] = (s[l]==s[r] and dp[l+1][r-1])
                
                if dp[l][r]:
                    length = r-l+1
                    if length>max_len:
                        max_len = length
                        best_left = l
                        best_right = r
            
        return s[best_left:best_right+1]