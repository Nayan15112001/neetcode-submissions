class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''
        dp  = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i][j] = True
        for l in range(n-1,-1,-1):
            for r in range(l,n):
                if s[l] == s[r]: 
                    if r-l+1<=2 or dp[l+1][r-1]:
                        dp[l][r] = True
                        if r-l+1 > len(ans):
                            ans = s[l:r+1]
        return ans
