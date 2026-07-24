class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_1,cost_2 = 0,0
        memo  = {}
        n = len(cost)
        def func(x):
            if x in memo:
                return memo[x]
            if x >= n:
                return 0
            memo[x]= cost[x] + min(func(x+1),func(x+2))
            
            return memo[x]
        cost1 = func(0)
        cost2 = func(1)

        return min(cost1,cost2)
