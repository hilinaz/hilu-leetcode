class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        mapping={}
        n=len(arr1)
        for i in range(len(arr2)):
            mapping[arr2[i]]=i
       
        def customSort(value):
            if value in mapping:
                return mapping[value]
            else:
                
                return n+value
        arr1.sort(key=customSort)
        return arr1
            
           
                
       

    


       
        