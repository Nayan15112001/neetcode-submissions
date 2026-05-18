class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(s.lower().split())
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        n = len(s)
        i = 0
        j = len(s)-1
        print(s)
        while i<j:
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True