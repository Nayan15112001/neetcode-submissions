import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            z = abs(x-y)
            if z>0:
                heapq.heappush(stones,-z)
            print(stones)

        if stones:
            return -stones[0]
        else:
            return 0