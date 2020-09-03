#N皇后
#DFS
#行，列，对角都只能有一个Q， 同一对角线和或差相等，不能用绝对值！！！
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(x_used,diagonal_a,diagonal_b,tmp):# x_used 竖列,diagonal_a 左斜,diagonal_b 右斜 
            y_i = len(x_used)
            if y_i == n:
                res.append(tmp)
                return
            for x_i in range(n):
                if x_i not in x_used and x_i-y_i not in diagonal_a and x_i + y_i not in diagonal_b:
                    solve(x_used + [x_i],diagonal_a + [x_i-y_i], diagonal_b + [x_i + y_i],tmp + ['.' * (x_i) + 'Q' + '.'*(n-1-x_i)])
        
        res = []
        solve([],[],[],[])
        return res
