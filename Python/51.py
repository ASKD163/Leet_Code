#N皇后

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(x_used,diagonal_a,diagonal_b,tmp):
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
