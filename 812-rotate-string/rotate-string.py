class Solution(object):
    def rotateString(self, s, goal):
        if s==goal:
            return  True
        val=""
        for i in range(len(s)):
            val+=s[i]
            if (s[i+1:]+val)==goal:
                return True
        return False

    