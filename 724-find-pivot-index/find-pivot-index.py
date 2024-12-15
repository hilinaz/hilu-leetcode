class Solution(object):
    def pivotIndex(self, nums):
        left=0
        
        right=sum(nums)
        for i in range(len(nums)):
            right-=nums[i]
            if i!=0:
                left+=nums[i-1]
            if left==right:
                return i
        return -1
            
           
           
       