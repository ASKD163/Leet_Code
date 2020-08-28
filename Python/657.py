# 机器人能否返回原点
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = [0,0]
        for i in moves:
            if i == 'R': count[0] += 1
            elif i == 'L': count[0] -= 1
            elif i == 'U': count[1] += 1
            else: count[1] -= 1
        
        if count == [0,0]: return True
        else: return False
