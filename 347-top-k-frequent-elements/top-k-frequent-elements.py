class Solution(object):
    def topKFrequent(self, nums, k):
        val = {}
        for num in nums:
            val[num] = val.get(num, 0) + 1

        sorted_vals = sorted(val.items(), key=lambda item: item[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_vals[i][0])
        
        return result