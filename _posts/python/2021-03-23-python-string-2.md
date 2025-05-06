---
title: "[python] 파이썬 string 활용-2"
date: 2021-03-23 18:58:28 +0900
categories: python
tags: python
header:
  teaser: "../../img/cover/python.png"
---



### BOJ 2941 - 크로아티아 알파벳

```python
x = list(input())
v = [x[0]]

for i in range(1,len(x)):
    if x[i]=='=':
        v.pop()
        if x[i-1]=='c':
            v.append('c=')
        elif x[i-1]=='s':
            v.append('s=')
        else: #z=이거나 dz=일때
            if i>=2 and x[i-2]=='d':
                v.pop()
                v.append('dz=')
            else:
                v.append('z=')
    elif x[i]=='-':
        v.pop()
        if x[i-1]=='c':
            v.append('c-')
        else:
            v.append('d-')
    elif x[i]=='j':
        if x[i-1]=='l':
            v.pop()
            v.append('lj')
        elif x[i-1]=='n':
            v.pop()
            v.append('nj')
        else:
            v.append('j')
    else:
        v.append(x[i])
        
print(len(v))
```

###### 다른 사람의 풀이 - 숏코딩

```python
import re
print(len(re.sub('c=|c-|dz=|d-|lj|nj|s=|z=','1',input())))
```

