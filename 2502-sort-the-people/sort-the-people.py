class Solution(object):
    def sortPeople(self, names, heights):

        for i in range(len(heights)):
            mini = i
            for j in range(i+1,len(heights)):
                if heights[mini]<heights[j]:
                    mini =j
            heights[mini],heights[i]=heights[i],heights[mini]
            names[mini],names[i]=names[i],names[mini]
        print(heights)
        return names


       