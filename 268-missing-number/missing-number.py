class Solution(object):
    def missingNumber(self, nums):
       n=len(nums)
       add=n * (n + 1) // 2
       sum_arr = sum(nums)
       missing = add - sum_arr
       if missing>0:
        return missing
       else:
        return 0

    
    
 


        