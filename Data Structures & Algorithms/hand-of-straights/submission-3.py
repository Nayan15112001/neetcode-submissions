class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand)
        count = Counter(hand)
        cards  = sorted(count.keys())
        for card in cards:
            
            freq = count[card]

            for i in range(groupSize):
                needed = card+i
                if count[needed]<freq:
                    return False
                
                count[needed]-=freq



        return True
            
