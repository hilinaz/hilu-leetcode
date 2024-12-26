class Solution(object):
    def sortedSquares(self, nums):
       newarr=[]
       start=0
       end=len(nums)-1
       while start<=end:
        if nums[start]**2>=nums[end]**2:
            newarr.append(nums[start]**2)
            start+=1
        else:
             newarr.append(nums[end]**2)
             end-=1
     
       return newarr[::-1]
        




