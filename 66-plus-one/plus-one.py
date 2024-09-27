class Solution(object):
    def plusOne(self, digits):
        val = "".join(map(str, digits))
        val = int(val) + 1
        return [int(digit) for digit in str(val)]