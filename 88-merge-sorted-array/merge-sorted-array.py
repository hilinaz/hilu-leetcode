class Solution(object):
    def merge(self,nums1, m, nums2, n):
        if m==0:
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
            return nums1
        
        elif n==0:
            return nums1
        j=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[i-m]
            j+=1
        return nums1.sort()

       
        
    

        
     
                
        
        
   
       