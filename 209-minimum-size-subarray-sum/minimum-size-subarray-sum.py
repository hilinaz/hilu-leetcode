class Solution(object):
    def minSubArrayLen(self, target, nums):
        left =0 
        summ = 0
        maxi =float('inf')
        if sum(nums)<target:
            return 0
        for right in range(len(nums)):
            summ+=nums[right]
            while summ >=target:
                maxi = min(maxi,right-left+1)
                summ -= nums[left]
                left +=1
       
        return maxi


            

       
     