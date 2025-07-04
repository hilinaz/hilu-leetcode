class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr)-1
        while low<= high and -1<high<len(arr) and -1<low<len(arr):
            mid = (low+high)//2
            if arr[mid] <=arr [high]:
                low+=1
            else:
                high-=1
        return high
            
       