class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Brute force
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
        return False
        """

        prevmap = {} #val:index 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n] = i
        return
