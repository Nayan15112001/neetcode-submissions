class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome = []
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for l in range(n-1,-1,-1):
            for r in range(l,n):
                if s[l] == s[r]:
                    if r-l+1<=2 or dp[l+1][r-1]:
                        dp[l][r] = True
                        palindrome.append(s[l:r+1])
        

        return len(palindrome)