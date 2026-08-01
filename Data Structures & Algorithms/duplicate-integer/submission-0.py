class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_mapping = {}
        for num in nums:
            if num not in number_mapping:
                number_mapping[num] = 1
            else:
                return True
        return False