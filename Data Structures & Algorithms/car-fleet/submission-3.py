class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hops = []
        res = 0
        n = len(position)
        
        maxpos,h = 0,0
        for i in range(n):
            maxpos = max(maxpos,position[i])
            h = (target-position[i])/speed[i]
            hops.append([position[i],h])
        hops.sort(reverse = True)
        print(hops) 
        stk = [hops[0]]
        for i in range(1,n):
            stk.append(hops[i])
            if stk[-1][1] <= stk[-2][1]:
                stk.pop()

        print(stk)
        return len(stk)

        