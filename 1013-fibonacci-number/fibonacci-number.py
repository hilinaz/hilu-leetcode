class Solution(object):
    memo={}
    def fib(self, n):
        if n==0 or n==1:
            return n
        if n in Solution.memo:
            return Solution.memo[n]
        Solution.memo[n]=self.fib(n-1)+self.fib(n-2)
        return Solution.memo[n]