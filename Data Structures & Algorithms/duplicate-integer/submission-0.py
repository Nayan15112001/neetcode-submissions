class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        print(count)
        for item,c in count.items():
            print(c)
            if c>1:
                return True
  
        return False