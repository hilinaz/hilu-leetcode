import itertools
class Solution(object):
    def permute(self, nums):
        permutations = set(itertools.permutations(nums))
        return permutations
        
        