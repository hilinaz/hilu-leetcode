class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        dic={}
        lis=[]
        if len(s)!=len(pattern):
            return False
        for i in range (len(s)):
            if pattern[i] not in dic:
                dic[pattern[i]]=s[i]
        for i in pattern:
            lis.append(dic[i])
        val=list(dic.values())
        if len(val)!=len(set(val)):
            return False


        for i in range(len(s)):
            if s[i]!=lis[i]:
                return False
        return True
    
        