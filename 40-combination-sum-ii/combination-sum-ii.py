class Solution(object):
    def combinationSum2(self, candidates, target):
   
    
        candidates.sort()  
        res = []

        def backtrack(start, current, total):
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue 

                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()
                prev = candidates[i] 

        backtrack(0, [], 0)
        return res
