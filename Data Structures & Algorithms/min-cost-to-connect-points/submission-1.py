import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list= {}
        hmap = {}

        for i in range(len(points)):
            hmap[i] = points[i]

        for i in range(len(points)):
            adj_list[i] = []
        
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                adj_list[i].append(j)

        
        visited = set()

        def man_distance(p1,p2):
            point1 = hmap[p1]
            point2 = hmap[p2]
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        heap = []
        heapq.heappush(heap,[0,0])
        total_dist = 0
        while heap and len(visited)< len(points):
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            total_dist +=distance
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dist = man_distance(node,nei)
                    heapq.heappush(heap,[dist,nei])
                    
        return total_dist