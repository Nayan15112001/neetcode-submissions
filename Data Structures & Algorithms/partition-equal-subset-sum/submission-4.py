class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum+=num
        
        if sum%2 !=0:
            return False
        target = sum/2
        dp ={}
        n = len(nums)

        def dfs(i,cursum):
            if (i,cursum) in dp:
                return dp[(i,cursum)]
            
            if cursum == target:
                return True
            if cursum>target or i==n:
                return False
            
            dp[(i,cursum)] = dfs(i+1,cursum) or dfs(i+1,cursum+nums[i])

            return dp[(i,cursum)]
        

        return dfs(0,0)
