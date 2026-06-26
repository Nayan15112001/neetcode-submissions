class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,sol = [],[]
        n = len(s)
        def ispalindrome(sol: list):
            print(sol)
            for s in sol:
                if s != s[::-1]:
                    return False
            return True

        def backtrack(i):
            if not ispalindrome(sol):
                return
            if i == n and ispalindrome(sol):
                res.append(sol[:])
                return

            for j in range(i,n):
                sol.append(s[i:j+1])
                backtrack(j+1)
                sol.pop()
            
        backtrack(0)
        return res
            
