class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            x=nums.index(min(nums))
            nums[x]=nums[x]*multiplier
        return nums
        