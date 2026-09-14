class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref = {}
        for n in nums:
            if n in ref:
                ref[n] += 1
            else:
                ref[n] = 1
        
        for key, value in ref.items():
            if value == max(ref.values()):
                return key
