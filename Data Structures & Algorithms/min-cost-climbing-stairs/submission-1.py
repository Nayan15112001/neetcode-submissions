class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo  = {}
        n = len(cost)
        def func(x):
            if x in memo:
                return memo[x]
            if x >= n:
                return 0
            memo[x]= cost[x] + min(func(x+1),func(x+2))
            
            return memo[x]
        
        return min(func(0),func(1))
