class Solution(object):
    def shortestToChar(self, s, c):
        answer = [0] * len(s)
        indices = [i for i, char in enumerate(s) if char == c]

        for i in range(len(s)):
            answer[i] = min(abs(i - idx) for idx in indices)

        return answer