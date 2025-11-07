class Solution(object):
    def partitionLabels(self, s):
        last_seen={}
        answer=[]
        for i in range(len(s)):
            last_seen[s[i]]=i
        maxi =0
        j=0
        for i in range(len(s)):
            maxi=max(last_seen[s[i]],maxi)
            if i ==maxi:
                answer.append(maxi-j+1)
                j=i+1
                maxi = 0
        return answer



        

      