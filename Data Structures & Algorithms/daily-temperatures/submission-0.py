class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        l = 0
        r = 1
        while l < n:
            while r<n-1 and temperatures[l] >= temperatures[r]:
                r+=1
                print(f'l:{l}')
                print(f'r:{r}')
            if temperatures[r] > temperatures[l]:     
                res.append(r-l)
            else:
                res.append(0)
            print(f'res:{res}')
            l+=1
            r=l
            
            
        return res