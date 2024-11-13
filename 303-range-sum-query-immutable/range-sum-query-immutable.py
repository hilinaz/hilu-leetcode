class NumArray(object):
    def __init__(self, nums):
        self.pres = []
        for i in range(len(nums)):
            if i == 0:
                self.pres.append(nums[i])
            else:
                self.pres.append(nums[i] + self.pres[-1])
        

    def sumRange(self, left, right):
        if left == 0:
            return self.pres[right]
        return self.pres[right] - self.pres[left - 1]
