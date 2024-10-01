class Solution(object):
    def minElement(self, nums):
        numss=list(map(str, nums))
        numsi=[]
        for i in numss:
            add=0
            for j in i:
                add+=int(j)
            numsi.append(add)
        return min(numsi)
        