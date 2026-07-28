class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.ans = ''
        def expand(l,r):
            while l>=0 and r<=n-1 and s[l] == s[r]:
                if r-l+1>len(self.ans):
                    self.ans =  s[l:r+1]
                l-=1
                r+=1
                

        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return self.ans