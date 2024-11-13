class Solution(object):
    def productExceptSelf(self, nums):
       val=[]
       num=0
       for i in range(len(nums)):
        if i ==0:
            val.append(1)
        else:
            val.append(val[-1]*nums[i-1])
      
       for j in range(len(nums)-1,-1,-1):
        if j==len(nums)-1:
            num=1
        else:
            num=num*nums[j+1]
        val[j]=val[j]*num
       return val


        
        
        


        