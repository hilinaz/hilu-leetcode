class Solution(object):
    def longestValidParentheses(self, s):
      
        maxi = 0
        O_count = 0
        C_count = 0
        for char in s:
            if char =='(':
                O_count+= 1
            else:
                C_count += 1

            if O_count==C_count:
                maxi = max(maxi, 2 * O_count)
            elif C_count>O_count:
                O_count = 0
                C_count = 0
        
        O_count=0
        C_count=0

        for i in range(len(s) - 1, -1, -1):
            char=s[i]
            if char=='(':
                O_count+= 1
            else:
                C_count +=1
            
            if O_count==C_count:
                maxi=max(maxi, 2 * O_count)
            elif O_count>C_count:
                O_count = 0
                C_count = 0
        
        return maxi
        