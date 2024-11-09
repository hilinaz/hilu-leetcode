class Solution(object):
    def twoSum(self, numbers, target):
        output=[]
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                output.append(i+1)
                output.append(j+1)
                return output
            elif numbers[i]+numbers[j]>target:
                j=j-1
            else:
                i=i+1


                
        