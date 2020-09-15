class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def DFS(pos):
            if pos == len(blank):#终止条件 全部填完
                return True
            i,j = blank[pos]
            b = (i//3)*3 + j//3
            rst = num - line[i] - column[j] - block[b] #剩余能填的数
            if not rst:
                return False #能填的数为空，有数填错，回溯删除已填的数
            for x in rst:
                line[i].add(x)
                column[j].add(x)
                block[b].add(x)
                board[i][j] = x #填入
                if DFS(pos+1):
                    return True
                line[i].remove(x)
                block[b].remove(x)
                column[j].remove(x)

        #初始化
        num = {'1','2','3','4','5','6','7','8','9'}
        line = [set() for i in range(9)]
        column = [set() for i in range(9)]
        block = [set() for i in range(9)] 
        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i,j))#标记需要填数的位置
                else:
                    line[i].add(board[i][j])
                    column[j].add(board[i][j])
                    block[(i//3)*3 + j//3].add(board[i][j])# 行，列，块已经用过的数

        DFS(0)
