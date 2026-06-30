class Solution:

    def __init__(self, w: List[int]):
        self.lst = []
        self.n = len(w)
        sum,prob = 0,0
        #calc total sum
        for num in w:
            sum+=num
        for i in range(len(w)):
            prob = int(w[i]/sum *100)
            for j in range(prob):
                self.lst.append(i)


    def pickIndex(self) -> int:
        return self.lst[random.randint(0,len(self.lst)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()