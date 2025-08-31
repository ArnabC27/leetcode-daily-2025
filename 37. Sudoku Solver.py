class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        unfilled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unfilled.append((i, j))
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3) * 3 + j//3].add(board[i][j])
        self._fill(0, unfilled, rows, cols, boxes, board)
        
    def _fill(self, index, unfilled, rows, cols, boxes, board):
        if index >= len(unfilled):
            return True
        x, y = unfilled[index]
        for num in '123456789':
            board[x][y] = num
            if (num in rows[x]) or (num in cols[y]) or (num in boxes[(x//3) * 3 + y//3]):
                    continue
            rows[x].add(num)
            cols[y].add(num)
            boxes[(x//3) * 3 + y//3].add(num)
            if self._fill(index + 1, unfilled, rows, cols, boxes, board):
                return True
            board[x][y] = '.'
            rows[x].remove(num)
            cols[y].remove(num)
            boxes[(x//3) * 3 + y//3].remove(num)
        return False
