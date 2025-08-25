class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        row, col = 0, 0
        directionUp = True  # True means moving up-right, False means down-left
        
        # Process each element in the matrix.
        for _ in range(m * n):
            result.append(matrix[row][col])
            if directionUp:
                # Move up-right.
                new_row = row - 1
                new_col = col + 1
                # Check for out-of-bound conditions.
                if new_col >= n:
                    row += 1
                    directionUp = False
                elif new_row < 0:
                    col += 1
                    directionUp = False
                else:
                    row, col = new_row, new_col
            else:
                # Move down-left.
                new_row = row + 1
                new_col = col - 1
                if new_row >= m:
                    col += 1
                    directionUp = True
                elif new_col < 0:
                    row += 1
                    directionUp = True
                else:
                    row, col = new_row, new_col
        return result
