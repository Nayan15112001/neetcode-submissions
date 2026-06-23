import heapq
class MedianFinder:

    def __init__(self):
        self.smallheap = []
        self.largeheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap,-num)
        heapq.heappush(self.largeheap,-heapq.heappop(self.smallheap))
        if len(self.largeheap)-len(self.smallheap)>1:
            heapq.heappush(self.smallheap,-heapq.heappop(self.largeheap))
        print(f"small heap:{self.smallheap}")
        print(f"large heap:{self.largeheap}")
        
    def findMedian(self) -> float:
        if len(self.smallheap)>len(self.largeheap):
            return -self.smallheap[0]
        elif len(self.largeheap)>len(self.smallheap):
            return self.largeheap[0]
        else:
            return (self.largeheap[0]+(-self.smallheap[0]))/2
        
                
        
        