class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def func(x):
            if x in memo:
                return memo[x]
            
            if x>=n:
                return 0
            
            curr = nums[x]+func(x+2)
            skip = func(x+1)

            memo[x] = max(curr,skip)

            return memo[x]
        
        return func(0)        