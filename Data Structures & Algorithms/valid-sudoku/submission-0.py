import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create dictionaries where the values are Hash Sets
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # Key will be a tuple: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Ignore empty cells
                if val == ".":
                    continue
                
                # Check for duplicates in our three sets
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[(r // 3, c // 3)]):
                    return False
                
                # If no duplicates, add the value to all three sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
                
        # If we check every cell and find no duplicates, the board is valid
        return True