class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,sol = [],[]
        def backtrack(i):
            res.append(sol[:])
            for j in range(i,n):
                sol.append(nums[j])
                backtrack(j+1)
                sol.pop()
        backtrack(0)
        return res
