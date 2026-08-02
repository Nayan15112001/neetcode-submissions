class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp  = {n:1}
        if s[0] == '0':
            return 0
        def ways(x):
            if x in dp:
                return dp[x]
            if x>=n:
                return 0
            
            if s[x] == '0':
                dp[x] = 0
            else:
                dp[x]=ways(x+1)
                if s[x] == '1' or (x+1<n and s[x] == '2' and s[x+1] in ("0123456")):
                    dp[x]+=ways(x+2)
            return dp[x]

        return ways(0)
            