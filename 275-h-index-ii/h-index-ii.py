class Solution(object):
    def hIndex(self, citations):
        def cite(num):
            count=0
            for i in citations:
                if i>=num:
                    count+=1
            return count>=num and count<=len(citations)
        low = 0
        high = citations[-1]
        while low<= high:
            mid = (low+high)//2
            if cite(mid):
                low = mid+1
            else:
                high=mid-1
        return high

