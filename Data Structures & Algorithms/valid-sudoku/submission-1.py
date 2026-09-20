class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check all rows
        for r in range(n):
            seen = set()
            for c in range(n):
                if board[r][c] in seen:
                    return False
                if board[r][c] != '.':
                    seen.add(board[r][c])
                
        # Check all columns
        for c in range(n):
            seen = set()
            for r in range(n):
                if board[r][c] in seen:
                    return False
                if board[r][c] != '.':
                    seen.add(board[r][c])
            
        # Check all squares 
        for offset_r in range(0, n, 3):
            for offset_c in range(0, n, 3):
                seen = set()
                for r in range(n // 3):
                    for c in range(n // 3):
                        if board[offset_r + r][offset_c + c] in seen:
                            return False
                        if board[offset_r + r][offset_c + c] != '.':
                            seen.add(board[offset_r + r][offset_c + c])
                        
        return True                