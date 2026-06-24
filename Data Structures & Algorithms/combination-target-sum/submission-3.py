class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res,sol = [],[]
        nums.sort()
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            elif curr_sum>target:
                return
            
            
            for j in range(i,n):
                sol.append(nums[j])
                backtrack(j,nums[j]+curr_sum)
                sol.pop()
        backtrack(0,0)
        return res
