---
title: "[python] 파이썬 기본수학 1-1"
date: 2021-03-25 18:58:28 +0900
tags: python
categories: python
header:
  teaser: "../../img/cover/python.png"
---



### BOJ 1712 - 손익분기점

```python
import math
a,b,c = map(int, input().split())
result = 0
if c<=b:
    result = -1
else:
    n = a/(c-b)
    if float(int(n)) == n:
        result = int(n) + 1
    else:
        result = int(math.ceil(n))
    
print(result)
```

