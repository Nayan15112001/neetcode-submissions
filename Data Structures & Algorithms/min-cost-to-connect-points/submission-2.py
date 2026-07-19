import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()

        def man_distance(p1,p2):
            point1 = points[p1]
            point2 = points[p2]
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
            for nei in range(len(points)):
                if nei not in visited:
                    dist = man_distance(node,nei)
                    heapq.heappush(heap,[dist,nei])
                    
        return total_dist