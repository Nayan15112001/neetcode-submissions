class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n  = len(digits)
        hmap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], 
        '9':['w','x','y','z']}
        res,sol = [],[]
        

        def backtrack(i,sol):
            if len(sol) == n:
                print(sol)
                s= ""
                for c in sol:
                    s+=c
                if s!= "":
                    res.append(s)
                return
            
            for c in hmap[digits[i]]:
                sol.append(c)
                backtrack(i+1,sol)
                sol.pop()
        backtrack(0,sol)
        return res

