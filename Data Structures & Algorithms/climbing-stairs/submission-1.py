class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
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