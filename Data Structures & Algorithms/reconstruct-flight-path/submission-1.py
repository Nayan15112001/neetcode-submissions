from collections import deque
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}
        ans  = []
        

        for i in range(len(tickets)):
            d_from,d_to = tickets[i]
            adj_list[d_from] = []
        
        for ticket in tickets:
            a,b = ticket
            heapq.heappush(adj_list[a],b)
        
        print(adj_list)
        def dfs(loc):
            while loc in adj_list and adj_list[loc]:
                k = heapq.heappop(adj_list[loc])
                dfs(k)
            ans.append(loc)
            
        dfs('JFK')

        return ans[::-1]