class Solution(object):
    def maxAscendingSum(self, nums):
        val = 0
        presum = []
        max_sum = 0
        
        for i in nums:
            val += i
            presum.append(val)
        
        start = 0
        end = 0
        
        while end < len(nums):
            if end > 0 and nums[end] <= nums[end - 1]:
                start = end 
            current_sum = presum[end] - (presum[start - 1] if start > 0 else 0)
            max_sum = max(max_sum, current_sum)
            end += 1
        
        return max_sum