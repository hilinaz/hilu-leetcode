class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("You cannot divide by zero.")
        
        if dividend == float('-inf') and divisor == -1:
            return 2147483647 

        is_negative_result = (dividend < 0) ^ (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        if is_negative_result:
            quotient = -quotient

        return max(-2147483648, min(2147483647, quotient))