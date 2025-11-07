class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while j<len(nums) and i<len(nums):
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            elif nums[i]!=0:
                i+=1
            j+=1
           
        return nums

       