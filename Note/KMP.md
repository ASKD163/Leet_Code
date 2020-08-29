# KMP

[KMP原理](https://www.bilibili.com/video/BV1Px411z7Yo/?spm_id_from=333.788.videocard.0)
[KMP算法](https://www.bilibili.com/video/BV1hW411a7ys?from=search&seid=1761274017871731059)

## 生成prefix table
生成prefix表（[5:32 - 10:10](https://www.bilibili.com/video/BV1kJ411u7pt?from=search&seid=1761274017871731059)）
```python
def prefixt(pattern):
    pre = [0] #首位
    i = 1 #从第二位开始比较
    j =0
    while (i < len(pattern)):
        if pattern[i] == pattern[j]: #相同 +1
            i += 1
            j += 1
            pre.append(j)
        else: #不同
            if j > 0: 
                j = pre[j-1]
            else:
                pre.append(j)
                i += 1
    pre.insert(0, -1)
    return pre
```
## KMP search
```python
def kmp_search(text,pattern):
    pre = prefixt(pattern)
    j = 0
    i = 0
    while (i < len(text)):
        if j == len(pattern) - 1 and text[i] == pattern[j]:
            print(i -j)#found
            j = pre[j]#继续向下匹配 
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            j = pre[j]
            if j == -1:
                i += 1
                j += 1
```
