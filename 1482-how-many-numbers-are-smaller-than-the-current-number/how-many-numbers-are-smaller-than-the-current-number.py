class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        vals =sorted(nums)
        ans = []
        mapped ={}
        for i in range(len(vals)):
            if vals[i] not in mapped:
                mapped[vals[i]]= i
        for i in nums:
            ans.append(mapped[i])
        return ans

        