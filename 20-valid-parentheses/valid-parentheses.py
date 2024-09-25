class Solution(object):
    def isValid(self, z):
        x = []
        y = {")": "(", "]": "[", "}": "{"}

        for a in z:
            if a in y.values():
                x.append(a)
            elif a in y.keys():
                if x and x[-1] == y[a]:
                    x.pop()
                else:
                    return False
            else:
                return False

        return len(x) == 0
            
