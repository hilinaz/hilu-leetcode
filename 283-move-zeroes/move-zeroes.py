class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=1
        temp=0
        while j<len(nums):
            if nums[i]==0 and nums[j]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                i+=1
                j+=1
        return nums


        