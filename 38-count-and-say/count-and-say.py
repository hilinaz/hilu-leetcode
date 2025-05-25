class Solution(object):
    def countAndSay(self, n):
        def count(s):
            start = 0
            end = 0
            res = ''
            while end < len(s):
                if s[start] == s[end]:
                    end += 1
                else:
                    res += str(end - start) + s[start]
                    start = end
          
            res += str(end - start) + s[start]
            return res
        
        prev = "1"
        for i in range(2, n + 1):
            prev = count(prev)
        return prev


                
