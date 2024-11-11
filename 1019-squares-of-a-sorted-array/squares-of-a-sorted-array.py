class Solution(object):
    def sortedSquares(self, nums):
        newarr=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]**2>=nums[j]**2:
                newarr.append(nums[i]**2)
                i+=1
            else:
                newarr.append(nums[j]**2)
                j-=1
        return newarr[::-1]
            


