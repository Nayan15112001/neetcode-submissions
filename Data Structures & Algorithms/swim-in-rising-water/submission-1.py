import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        n = len(grid)
        heapq.heappush(heap,(grid[0][0],(0,0)))
        visited = set()
        min_cost = grid[n-1][n-1]
        options= [(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            cost,position = heapq.heappop(heap)
            row,col = position
            if position == (n-1,n-1):
                print(min_cost)
                print(cost)
                return max(cost,min_cost)
            if position in visited:
                continue
            min_cost = max(min_cost,cost)
            visited.add((row,col))
            
            for option in options:
                r,c = option
                nr = row+r
                nc = col+c
                if nr>=0 and nc>=0 and nr<n and nc<n and (nr,nc) not in visited:
                    heapq.heappush(heap,(grid[nr][nc],(nr,nc)))

        
        return min_cost
            