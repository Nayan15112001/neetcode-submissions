class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for val,c in count.items():
            if c>1:
                return True

        return False