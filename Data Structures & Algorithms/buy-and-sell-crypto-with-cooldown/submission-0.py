class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =  len(prices)
        dp = {}
        def dfs(i,buying):
            if (i,buying) in dp:
                return dp[(i,buying)]

            if i>=n:
                return 0 

            #buying
            if buying:
                take = -prices[i] + dfs(i+1,False)
                skip = dfs(i+1,True)
            #selling
            else:
                take = prices[i] + dfs(i+2,True)
                skip = dfs(i+1,False)
            dp[(i,buying)] = max(take,skip)
            return dp[(i,buying)]
        
        return dfs(0,True)
            