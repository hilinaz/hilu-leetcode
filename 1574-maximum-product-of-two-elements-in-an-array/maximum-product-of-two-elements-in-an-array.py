class Solution(object):
    def maxProduct(self, nums):
        for i in range(len(nums)):
            for j in range(1,len(nums)-i):
                if nums[j-1]>nums[j]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        return (nums[-1]-1)*(nums[-2]-1)