class Solution(object):
    def findAnagrams(self, s, p):
        left =0 
        right = len(p)-1
        seen= Counter(s[:len(p)-1])
        seen_p =Counter(p)
        ans = []
        while right<len(s):
            if s[right] in seen:
                seen[s[right]]+=1 
            else:
                seen[s[right]]=1
            if seen ==seen_p:
                ans.append(left)
            if  seen[s[left]]==1:
                del seen[s[left]]
            else:

                seen[s[left]]-=1
            left+=1
            right+=1
        return ans


        
        
            

           
               

        


       
        