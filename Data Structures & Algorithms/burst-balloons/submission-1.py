class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = {}
        def dfs(l,r):
            if (l,r) in dp:
                return dp[(l,r)]
            
            if l>r:
                return 0
            
            ans = 0
            for k in range(l, r+1):

                left = dfs(l, k-1)
                right = dfs(k+1, r)
                burst_k_last = nums[l-1] * nums[k] * nums[r+1]
                total = left + burst_k_last + right
                ans = max(ans,total)
            
            dp[(l,r)] = ans
            
            
            

            return dp[(l,r)]
        
        return dfs(1,n-2)

