class Solution(object):
    def partitionLabels(self, s):
        last_seen = {}
        for i in range(len(s)):
            last_seen[s[i]] = i
        
        result = []
        start, end = 0, 0

        for i in range(len(s)):
            end = max(end, last_seen[s[i]])

            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result
