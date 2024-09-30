class Solution(object):
    def findWordsContaining(self, words, x):
        lis=[]
        for i in range(len(words)):
            if x in words[i]:
                lis.append(i)

       
        return lis