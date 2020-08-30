#分三块处理,row(i)，column(j),block((i//3) + (j//3)*3)
# [0,1,2,
#  3,4,5,
#  6,7,8]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        column = [{} for i in range(9)]
        block = [{} for i in range (9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num != '.':
                    row[i][num] = row[i].get(num, 0)+1
                    column[j][num] = column[j].get(num, 0) + 1
                    block[(i//3)+(j//3)*3][num] = block[(i//3)+(j//3)*3].get(num, 0) + 1
                if row[i].get(num) > 1 or column[j].get(num) > 1 or block[(i//3)+(j//3)*3].get(num)  > 1:
                    return False
        
        return True
