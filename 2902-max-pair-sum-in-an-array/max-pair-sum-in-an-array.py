class Solution(object):
    def maxSum(self, nums):
        val = {}
        lis = []
        
        for i in nums:
            num = max(str(i))
            if num not in val:
                val[num] = []
            val[num].append(i)

        max_sum = -1

        for largest_digit in val:
            if len(val[largest_digit]) > 1:
                val[largest_digit].sort(reverse=True)
                current_sum = val[largest_digit][0] + val[largest_digit][1]
                max_sum = max(max_sum, current_sum)

        return max_sum if max_sum != -1 else -1