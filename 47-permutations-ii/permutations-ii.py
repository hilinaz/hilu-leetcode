import itertools
class Solution(object):
    def permuteUnique(self, nums):
        val=list(itertools.permutations(nums))
        return set(val)
        
        