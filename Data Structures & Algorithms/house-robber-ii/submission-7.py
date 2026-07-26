class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def func1(x):
            
            if x in memo:
                return memo[x]
            
            if x>=n:
                return 0

            take = nums[x]+func1(x+2)
            skip = func1(x+1)
            memo[x] = max(take,skip)

            # print(memo)

            return memo[x]
        memo1 = {}
        def func2(x):
            print(x)
            if x>=n-1:
                return 0
            
            if x in memo1:
                return memo1[x]
            
            

            take = nums[x]+func2(x+2)
            skip = func2(x+1)
            memo1[x] = max(take,skip)

            return memo1[x]
        
        
        
        return max(func1(1),func2(0))
            