import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        hq = []
        for num in self.nums:
            heapq.heappush(hq,num)
        ans = 0
        print(hq)
        count_to_pop = len(hq)-self.k+1
        for i in range(count_to_pop):
            ans = heapq.heappop(hq)
        
        return ans


            
