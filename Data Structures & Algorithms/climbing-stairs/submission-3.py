class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n:1}
        def rec(x):
            if x in memo:
                return memo[x]
            if x>n:
                return 0
            if x == n:
                return 1
            memo[x] =rec(x+2) + rec(x+1) 
            return memo[x]
        
        return rec(0)