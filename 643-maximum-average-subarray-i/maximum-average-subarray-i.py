class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums)==1:
            return nums.pop()
        maxaverage=float('-inf')
       
        left=0
        right=k-1
        Total=float(sum(nums[left:right+1]))
        maxaverage=max(maxaverage,Total/k)
        while right<len(nums)-1:
            Total-=nums[left]
            left+=1
            right+=1
            Total+=nums[right]
            maxaverage=max(maxaverage,Total/k)
        return maxaverage
            

            
            
        

        

            
        