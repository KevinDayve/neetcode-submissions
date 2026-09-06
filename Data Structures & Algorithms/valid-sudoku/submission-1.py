class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We will check if row contains duplicate;
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        # We will now check if column contains any duplicate;
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for rowOffset in range(3):
                    for colOffset in range(3):
                        row = boxRow * 3 + rowOffset
                        col = boxCol * 3 + colOffset

                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        return True