class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def func(x):
            if x in memo:
                return memo[x]
            
            if x>=n:
                return 0
            
            memo[x] = nums[x]+max(func(x+2),func(x+3))
            return memo[x]
        
        print(func(0))
        print(func(1))
        return max(func(0),func(1))
        