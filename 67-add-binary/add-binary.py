class Solution(object):
    def addBinary(self, a, b):
    
        val = int(a, 2) + int(b, 2)
  
        return bin(val)[2:]

