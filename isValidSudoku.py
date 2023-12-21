from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if(board[r][c] == "."):
                continue
            
            curr = board[r][c]
            if(curr in rows[r] or curr in cols[c] or curr in squares[(r//3, c//3)]):
                return False
            else:
                rows[r].add(curr)
                cols[c].add(curr)
                squares[(r//3, c//3)].add(curr)
        
    return True


print(isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]))  # True