class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            # print(n)
            if n not in s:
                s.add(n)
            else:
                return True
            # print(s)
        return False