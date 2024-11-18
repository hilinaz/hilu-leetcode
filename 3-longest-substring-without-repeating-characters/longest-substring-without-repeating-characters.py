class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chara=set()
        left=0
        length=0
        for i in s:
            while i in chara:
                chara.remove(s[left])
                left+=1
            chara.add(i)
            length=max(length,len(chara))
        return length
            
           