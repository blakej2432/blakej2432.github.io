---
title: "[백준] 10870 - 피보나치 수 5"
date: 2021-04-07 09:58:28 +0900
tags: python
comments: true
published: true
categories: boj
typora-copy-images-to: ..\..\img
header:
  teaser: "../../img/cover/boj.png"
---

### 1. 요약

피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

for 문으로도 풀 수 있지만, 재귀를 사용하여 풀어보고자 한다.



### 2. 아이디어

>  n이 0과 1인 경우를 제외하고, Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.



### 3. 코드

```python
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))
```

