class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n:1,n-1:1}
        def rec(n):
            if n in dp:
                return dp[n]
            dp[n] = rec(n+1) + rec(n+2)
            return dp[n]
        return rec(0)