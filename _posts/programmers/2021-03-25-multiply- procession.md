---
title: "[프로그래머스] 행렬의 곱셈"
date: 2021-03-25 18:58:28 +0900
tags: python
categories: programmers
header:
  teaser: "../../img/cover/programmers.png"
---

```python
def solution(arr1, arr2):
    answer = []
    for i in arr1:
        x = []
        for k in range(len(arr2[0])):
            n = 0
            for j in enumerate(arr2):
                n += i[j[0]] * j[1][k]
            x.append(n)
        answer.append(x)
           
    return answer
```

