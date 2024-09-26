class Solution(object):
    def twoSum(self, nums, target):
        val={}
        for i, num in enumerate(nums):
            add=  target-num
            if add in val:
                return([i,val[add]]) 
            else:
                val[num]=i
        return []