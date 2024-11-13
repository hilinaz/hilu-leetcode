class Solution(object):
    def pivotIndex(self, nums):
        pre = []
        post = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre.append(0)
            else:
                pre.append(pre[-1] + nums[i - 1])
        
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                post[j] = 0
            else:
                post[j] = post[j + 1] + nums[j + 1]

        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i
        return -1
