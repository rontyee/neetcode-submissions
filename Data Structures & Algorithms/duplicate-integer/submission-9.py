class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = dict()
        for num in nums:
            if num in hMap:
                return True
            hMap[num] = True
        return False