class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        dp = {}
        
        if n1+n2!=len(s3):
            return False
        def dfs(i1,i2):
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            
            ans = False

            if i1== n1 and i2== n2:
                return True

            
            if i1<=n1-1 and s1[i1] == s3[i1+i2]:
                ans = dfs(i1+1,i2)
            
            if i2<=n2-1 and s2[i2] == s3[i1+i2]:
                ans =  ans or dfs(i1,i2+1)
            
            dp[(i1,i2)] = ans
            return dp[(i1,i2)]
        
        return dfs(0,0)