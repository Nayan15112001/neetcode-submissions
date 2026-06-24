class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res,sol = [],[]
        
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            elif curr_sum>target:
                return
            elif i == n:
                return
            
            backtrack(i+1,curr_sum)

            sol.append(nums[i])
            curr_sum+=nums[i]
            backtrack(i,curr_sum)
            sol.pop()
        backtrack(0,0)
        return res
