class Solution(object):
    def compress(self, chars):
        right=0
        left=0
        count=0
        s=""
        while right<len(chars):
            if chars[right]==chars[left]:
                right+=1
                count+=1
            if right==len(chars) or   (chars[right]!=chars[left]) :
                s+=chars[left]
                if count>1:
                    s+=str(count)
                
                left=right
                count=0
        for i in range(len(s)):
            if i <len(chars):
                chars[i]=s[i]
            
        return len(s)
        
        

        