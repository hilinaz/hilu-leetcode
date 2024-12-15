class Solution(object):
    def twoSum(self, numbers, target):
        output=[]
        right=len(numbers)-1
        left=0

        while right>left:
            if numbers[right]+numbers[left]==target:
                output.append(left+1)
                output.append(right+1)
                return output
            elif numbers[right]+numbers[left] >target:
                right-=1
            else:
                left+=1
            










                
        