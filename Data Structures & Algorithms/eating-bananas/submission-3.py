class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        sum= 0
        for i in range(n):
            sum+=piles[i]
        print(sum)
        res = sum
        l,r = 1,sum
        
        while l<r :
            m = l + ((r-l)//2)
            print(f'm:{m}')
            time = 0
            for i in range(n):
                time += math.ceil(piles[i]/m)
                print(f"time:{time}")
            
            if time<=h:
                res = min(res,m)
                print(f"res:{res}")
                r = m 
            else:
                l = m+1
        return res
            

                

