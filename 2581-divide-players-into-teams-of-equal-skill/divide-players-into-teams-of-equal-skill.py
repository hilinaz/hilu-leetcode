class Solution(object):
    def dividePlayers(self, skill):
        total = sum(skill)
        noOfTeam = len(skill)/2
        skillSum =total /noOfTeam 
        prod =0
        if total % noOfTeam!=0:
            return -1
        skill.sort()
        j=len(skill)-1
        for i in range(len(skill)/2):
            if skill[j]+skill[i]==skillSum:
                prod+=skill[j]*skill[i]
                j-=1
            else:
                return -1
        return prod 


        
        



     
        