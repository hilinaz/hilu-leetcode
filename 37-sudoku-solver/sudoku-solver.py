class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

    
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empties.append((r, c))

        def get_possible_values(r, c):
            box_idx = (r // 3) * 3 + (c // 3)
            return {str(x) for x in range(1, 10)} - rows[r] - cols[c] - boxes[box_idx]

        def backtrack():
            if not empties:
                return True

            # Choose the cell with the fewest options (MRV heuristic)
            empties.sort(key=lambda pos: len(get_possible_values(*pos)))
            r, c = empties.pop(0)
            box_idx = (r // 3) * 3 + (c // 3)

            for val in get_possible_values(r, c):
                board[r][c] = val
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

                if backtrack():
                    return True

                # Backtrack
                board[r][c] = '.'
                rows[r].remove(val)
                cols[c].remove(val)
                boxes[box_idx].remove(val)

            empties.insert(0, (r, c))
            return False

        backtrack()
