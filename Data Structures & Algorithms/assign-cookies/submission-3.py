class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n1 = len(g)
        n2 = len(s)
        s.sort(reverse = True)
        g.sort(reverse = True)
        print(s)
        print(g)
        n = min(n1,n2)
        count = 0
        i,j = 0,0
        while i<n1 and j<n2:
            if s[j]>=g[i]:
                j+=1
                count+=1           
            
            i+=1
        
        return count