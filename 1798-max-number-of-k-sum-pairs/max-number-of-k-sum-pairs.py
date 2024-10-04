class Solution(object):
    def maxOperations(self, nums, k):
        num_count = {}
        operation_count = 0
        
        for number in nums:
            num_count[number] = num_count.get(number, 0) + 1
        
        for num in list(num_count.keys()):
            if num in num_count:
                complement = k - num
                
                if complement in num_count:
                    if num == complement:
                        operation_count += num_count[num] // 2
                    else:
                        pairs = min(num_count[num], num_count[complement])
                        operation_count += pairs
                    
                    del num_count[num]
                    if complement != num:
                        del num_count[complement]
        
        return operation_count