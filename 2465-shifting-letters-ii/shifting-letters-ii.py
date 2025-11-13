class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prex =[0]*len(s)
        for change in shifts:
            if change[2]==0:
                prex[change[0]]-=1
                if change[1]<len(s)-1:
                    prex[change[1]+1]+=1  
            else:
                prex[change[0]]+=1
                if change[1]<len(s)-1:
                    prex[change[1]+1]-=1 
        for i in range(1,len(prex)):
            prex[i]=prex[i]+prex[i-1]
        s=list(s)
        for i in range (len(s)):
            order = ord(s[i])-ord('a')
            order+=prex[i]
            order%=26
            s[i]=chr(order+ord('a'))
        
            
            

        
            
         
        return ''.join(s)
    

        