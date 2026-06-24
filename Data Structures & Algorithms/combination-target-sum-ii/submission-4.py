class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res,sol = [],[]
        candidates.sort()
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            if curr_sum>target:
                return
            
            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                sol.append(candidates[j])
                backtrack(j+1,curr_sum+candidates[j])
                sol.pop()
        backtrack(0,0)
        return res