class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.start = 0
        self.length = 0
        self.end = 0

        def expand(l,r):
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > self.length:
                    self.length = r-l+1
                    self.start = l
                    self.end = r
                l-=1
                r+=1
        
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        
        return s[self.start:self.end+1]

