class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append([value,timestamp])
        else:
            self.hmap[key]=[[value,timestamp]]
        print(self.hmap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        nums = self.hmap[key]
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            m = l + ((r-l)//2)
            if nums[m][1] == timestamp  :
                return nums[m][0]
            elif nums[m][1]<timestamp:
                l = m+1
            else:
                r = m-1
    
        return nums[r][0] if r!= -1 else ""
        
