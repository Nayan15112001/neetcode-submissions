class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol  =[],[]
        n = len(nums)
        used = ['F']*n
        print(used)
        def backtrack(i):
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for j in range(n):
            # if the number is already picked you want to skip
                if used[j] == 'T':
                    continue
                #choose the number
                sol.append(nums[j])
                used[j] = 'T'
                
                #backtrack
                backtrack(j+1)

                #unchoose
                sol.pop()
                used[j] = 'F'
                
        backtrack(0)
        return res