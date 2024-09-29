class Solution(object):
    def canJump(self, nums):
        if len(nums) <= 1:
            return True
        
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            jump = nums[i]  
            max_reachable = max(max_reachable, i + jump)
            
            if max_reachable >= len(nums) - 1:
                return True
        
        return False