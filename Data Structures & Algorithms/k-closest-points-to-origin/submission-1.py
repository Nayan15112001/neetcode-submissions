import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        dist_points = []
        ans = []
        for i in range(n):
            x,y = points[i][0],points[i][1]
            dist = (x**2 + y**2)**1/2
            heapq.heappush(dist_points,(-dist,[x,y]))
            if len(dist_points)>k:
                heapq.heappop(dist_points)

        print(dist_points)
        
        while k:
            dist,coords = heapq.heappop(dist_points)
            ans.append(coords)
            k-=1


        return ans