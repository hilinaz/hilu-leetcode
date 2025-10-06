class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        n=len(piles)//3
        count =0
        j=1

        for i in range(n):
            count += piles[j]
            j+=2
        return count 


        

       
        