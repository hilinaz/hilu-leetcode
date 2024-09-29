class Solution(object):
    def reverseOnlyLetters(self, s):
        val = [char for char in s if char.isalpha()][::-1]
        j = 0
        s1 = ""

        for i in range(len(s)):
            if s[i].isalpha():
                s1 += val[j]
                j += 1
            else:
                s1 += s[i]

        return s1