class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = max_count = 0
        for num in nums:
            hm[num] += 1
            if hm[num] > max_count:
                max_count = hm[num]
                res = num
        return res