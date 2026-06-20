from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        heap = []
        for cnt in counter.values():
            heapq.heappush(heap,-cnt)
        q = deque()
        time = 0
        while heap or q:
            time+=1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt: 
                    q.append([cnt,time+n])
 
            if q and q[0][1] == time:
                val,t = q.popleft()
                heapq.heappush(heap,val)
        return time
        