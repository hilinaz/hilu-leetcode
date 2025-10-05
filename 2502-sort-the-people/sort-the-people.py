class Solution(object):
    def sortPeople(self, names, heights):

        for i in range(1,len(heights)):
            key = heights[i]
            key_n =names[i]
            j=i-1
            while j>=0 and heights[j]<key:
                heights[j+1]=heights[j]
                names[j+1]=names[j]
                j-=1
            heights[j+1]=key
            names[j+1]=key_n
        print(heights)
        return names
        