class Solution(object):
    def pancakeSort(self, arr):
        flips=[]
       
     
        for i in range(len(arr),0,-1):
            maxi= max(arr[:i])
            k = arr.index(maxi)+1 
            if k==i:
                continue
            if k >1:
                arr[:k]=arr[:k][::-1]
                flips.append(k)
            arr[:i] = arr[:i][::-1]
            flips.append(i) 
        return flips

            

       
        
        
     


       
        