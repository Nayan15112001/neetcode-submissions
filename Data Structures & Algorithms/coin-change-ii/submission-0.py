class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        def dfs(i,amt):
            if (i,amt) in dp:
                return dp[(i,amt)]
            
            if i == n :
                return 0
            
            if amt == 0:
                return 1
            
            if amt<coins[i]:
                take = 0
            else:
                take = dfs(i,amt-coins[i])
            skip = dfs(i+1,amt)

            dp[(i,amt)] = take+skip
            return dp[(i,amt)]
        
        return dfs(0,amount)

        # dp = [[0] *(amount+1) for _ in range(n)]
    
        # for i in range
        #         if i-c<0:
        #             continue
                
        #         take = dp[i][amount-coins[i]]
        #         skip = dp[i+1][amount]

        #         dp[i][amount] = take+skip
                
        # return dp[0][amount]
            
