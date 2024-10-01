class Solution(object):
    def getSneakyNumbers(self, nums):
        unique=[]
        s=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
            else:
                s.append(i)
        return s
        