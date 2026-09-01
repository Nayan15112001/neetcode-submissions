class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        n = len(nums)

        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= n-1:
                return True

            take = False
            if nums[i] == 0:
                return False
            for x in range(1,nums[i]+1):
                take = dfs(x+i)
                if take:
                    break
            print(i,take)
            dp[i] = take
            return dp[i]
        
        return dfs(0)
