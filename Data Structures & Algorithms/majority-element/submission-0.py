class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        possible_candidate = None
        count = 0
        for num in nums:
            if count == 0:
                possible_candidate = num
            if num == possible_candidate:
                count += 1
            else:
                count -= 1
        return possible_candidate
