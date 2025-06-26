class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        def backtrack(rem, curr, indx):
            if rem == 0:
                ans.append(list(curr))
                return

            if rem < 0:
                return

            for i in range(indx, len(candidates)):
                candidate = candidates[i]
                curr.append(candidate)
                backtrack(rem - candidate, curr, i)
                curr.pop()

        backtrack(target, [], 0)
        return ans