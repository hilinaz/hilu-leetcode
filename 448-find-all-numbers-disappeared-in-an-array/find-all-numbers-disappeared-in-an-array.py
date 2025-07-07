
class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans=[]
        num_map = Counter(nums)
        for i in range(1,len(nums)+1):
            if i not in num_map:
                ans.append(i)
        return ans