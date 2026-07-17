import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}
        heap = []
        for i in range(n):
            adj_list[i+1] = []

        for time in times:
            adj_list[time[0]].append([time[1],time[2]])
        
        heapq.heappush(heap,[0,k])
        seen = set()
        max_time = 0
        while heap:
            
            time,node = heapq.heappop(heap)

            if node in seen:
                continue
            
            max_time = max(time,max_time)
            seen.add(node)
            for nei in adj_list[node]:
                if nei[0] not in seen:
                    heapq.heappush(heap,[nei[1]+time,nei[0]])
        
        if len(seen) == n:
            return max_time
        return -1

        
        