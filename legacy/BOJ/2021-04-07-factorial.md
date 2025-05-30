---
title: "[백준] 10872 - 팩토리얼"
date: 2021-04-07 09:58:28 +0900
tags: python
categories: boj
header:
  teaser: "../../img/cover/boj.png"
---

### 1. 요약

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
for 문으로도 풀 수 있지만, 재귀를 사용하여 풀어보고자 한다.



### 2. 아이디어

>  n이 0과 1인 경우를 제외하고, N! 은 N*(N-1)! 로 정의할 수 있다.



### 3. 코드

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(int(input())))
```

