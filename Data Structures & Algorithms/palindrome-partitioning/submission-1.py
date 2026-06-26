class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,sol = [],[]
        n = len(s)
        def ispalindrome(s: list):
            if s != s[::-1]:
                return False
            return True

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            for j in range(i,n):
                if not ispalindrome(s[i:j+1]):
                    continue
                sol.append(s[i:j+1])
                backtrack(j+1)
                sol.pop()
            
        backtrack(0)
        return res
            
