from typing import List


class Solution:
    def in_bounds(self, r: int, c: int, rows: int, cols: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if self.in_bounds(nr, nc, rows, cols) and board[nr][nc] > 0:
                            live_neighbors += 1

                if board[r][c] == 1:
                    # 1 → 0: mark as 3, 1 → 1: mark as 2
                    board[r][c] = 2 if 2 <= live_neighbors <= 3 else 3
                else:
                    # 0 → 1: mark as -2
                    board[r][c] = -2 if live_neighbors == 3 else -3

        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if abs(board[r][c]) == 2 else 0
