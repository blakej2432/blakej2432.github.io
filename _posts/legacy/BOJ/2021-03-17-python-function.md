---
title: "[백준] 함수-2"
date: 2021-03-17 18:58:28 +0900
categories: boj
tags: python
header:
  teaser: "../../img/cover/boj.png"
---



### 백준 1065  - 한수

한수일 때 `True` 를 리턴하는 함수를 먼저 작성한 후, n의 경우의 수를 나누어서 `if`문으로 한수의 개수를 세는 로직으로 작성하였다.

```python
n = int(input())
count = 0

# 양의정수m 대입시 한수가 맞는지를 출력
def d(m):
    # 세자리수라고 가정(배열에 3개의 숫자)
    a = list(map(int,str(m)))
    if len(a)==3:
        if a[1]-a[0]==a[2]-a[1]:
            return True
        else:
            return False
    else:
        return False
        
# n보다 작거나 같은 한수의 개수
if n<100:
    count = n
elif 100<=n<=1000:
    count = 99
    for i in range(100,n+1):
        if d(i):
            count += 1
    
print(count)
```

**아래과 같이 여러자리 숫자를 각자리의 숫자로 이루어진 배열로 만들 수 있다.**

```python
m = 123
a = list(map(int,str(m)))
print(a)
## [1,2,3]
```
