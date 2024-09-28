class Solution(object):
    def countDigits(self, num):
        count=0
        for i in str(num):
            if num%int(i)==0:
                count+=1
        return count
        

        