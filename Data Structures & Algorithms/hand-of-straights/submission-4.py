class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand)
        count = Counter(hand)
        heapq.heapify(hand)


        while hand:
            minval = heapq.heappop(hand)
            if count[minval] == 0:
                continue
            freq = count[minval]
            for i in range(groupSize):
                needed = minval+i
                if count[needed]<freq:
                    return False
                
                count[needed]-=freq



        return True
            
