class Solution(object):
    def stableMountains(self, height, threshold):
       i=0
       mount=[]
       while i<len(height):
        if height[i]>threshold and i!=len(height)-1:
            mount.append(i+1)
        i+=1
       return mount

        