class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n+1: 0, n:1, n-1:1}
        def rec(x):
            if x in memo:
                return memo[x]
            if x>n:
                return 0
            if x == n:
                return 1
            memo[x] = rec(x+1) + rec(x+2)
            return memo[x]
        
        return rec(0)