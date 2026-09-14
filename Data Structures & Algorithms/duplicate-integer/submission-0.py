class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """res = {}
        for n in nums:
            if n in res:
                return True
            else:
                res[n] = 1
        return False    """
        res = set()
        for n in nums:
            if n in res: 
                return True
            res.add(n)
        return False    