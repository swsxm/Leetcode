from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = [set() for _ in range(9)]
        check_col = [set() for _ in range(9)]

        # could use default dict
        check_square = dict()  # (row, col)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                square_pos = (i // 3, j // 3)
                if val == ".":
                    continue

                if (
                    val in check_row[i]
                    or val in check_col[j]
                    or val in check_square.get(square_pos, [])
                ):
                    return False
                check_row[i].add(val)
                check_col[j].add(val)
                if square_pos in check_square:
                    check_square[square_pos].add(val)
                else:
                    check_square[square_pos] = {val}
        return True


testcase = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

Test = Solution()
print(Test.isValidSudoku(testcase))
