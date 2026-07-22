import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for edge in flights:
            adj_list[edge[0]].append([edge[1],edge[2]])
        heap = []
        heapq.heappush(heap,(0,src,0))

        min_cost = 0
        while heap:
            cost,node,flights_used = heapq.heappop(heap)
            if node == dst:
                return cost
            
            if flights_used == k+1:
                continue
            
            for nei,n_cost in adj_list[node]:
                    heapq.heappush(heap,(n_cost+cost,nei,flights_used+1))
        return -1










        