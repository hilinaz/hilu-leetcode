class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
   
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            line = ""

     
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                gaps = num_words - 1
                space, extra = divmod(total_spaces, gaps)

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space + (1 if k < extra else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res
