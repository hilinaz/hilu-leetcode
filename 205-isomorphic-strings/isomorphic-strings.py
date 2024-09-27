class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}
        dics={}
        val = ""
        vals=""

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
        for i in range(len(s)):
            if t[i] not in dics:
                dics[t[i]] = s[i]
        for i in s:
            val += dic[i]
        for i in t:
            vals += dics[i]
        return val == t and vals==s