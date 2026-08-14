class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        nums2 = [-num for num in nums]
        def dfs(i,amt):
            if (i,amt) in dp:
                return dp[(i,amt)]
            
            if i == n:
                if amt == target:
                    take = 1
                else:
                    take =  0
            
            else:
                take = dfs(i+1,nums[i]+amt) + dfs(i+1,nums2[i]+amt)
            
            dp[(i,amt)]  = take
            return dp[(i,amt)]

        return dfs(0,0)