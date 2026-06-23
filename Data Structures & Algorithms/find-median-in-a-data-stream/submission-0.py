import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,num)

    def findMedian(self) -> float:
        temp = self.heap.copy()
        n = len(self.heap)
        print(n)
        first,second = 0,0
        if n%2==0:
            for i in range(n):
                x = heapq.heappop(temp)
                if i+1 == n//2:
                    first = x
                    second = heapq.heappop(temp)
                    print(f"first:{first},second:{second}")
                    break
           
            return (first+second)/2
        else:
            for i in range(n):
                x = heapq.heappop(temp)
                if i+1 == (n//2)+1:
                    first = x
                    break
            
            return first
                
        
        