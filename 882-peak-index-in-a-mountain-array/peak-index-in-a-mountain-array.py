class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr)-1
        while low<= high:
            mid = (low+high)//2
            if arr[mid] <=arr [high]:
                low+=1
            else:
                high-=1
        return high
            
       