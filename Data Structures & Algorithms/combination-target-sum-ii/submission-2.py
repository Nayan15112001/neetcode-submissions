class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res,sol = [],[]
        candidates = sorted(candidates)
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            if i==n or curr_sum>target:
                return
            
            
            
            sol.append(candidates[i])
            backtrack(i+1,candidates[i]+curr_sum)
            sol.pop()

            while i<n-1 and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,curr_sum)

        backtrack(0,0)
        return res