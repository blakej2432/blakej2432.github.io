---
title: "[백준] 1929 - 소수 구하기(에라토스테네스의 체)"
date: 2021-04-06 18:58:28 +0900
tags: python
comments: true
published: true
categories: boj
typora-copy-images-to: ..\..\img
header:
  teaser: "../../img/cover/boj.png"
---

### 1. 요약

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.  (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.



### 2. 아이디어

> 기존의 두번 반복문을 도는 방식을 사용하면 시간 초과가 난다. 따라서 이 문제는 **에라토스테네스의 체**를 이용하여 풀어야 하는 문제이다.

에라토스테네스의 체는 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법이다.

- 먼저 1을 제거한 후, 2를 소수로 채택한 후 2의 배수를 모두 지운다. 
- 3을 소수로 채택한 후, 3의 배수를 모두 지운다.
- 5를 소수로 채택한 후, 5의 배수를 모두 지운다. 
- (반복)...
- 그림으로 표현하면 다음과 같다.

![image-20210406071623230](/img/image-20210406071623230.png)



### 3. 코드

```python
import math
def isPrime(m,n):
    # 0과 1을 제외한 모든 수에 대하여 소수 판별
    a = [False,False] + [True]*(n-1)
    
    #에라토스테네스의 체
    for i in range(2,int(math.sqrt(n))+1):
        if a[i]:
            # i를 제외한 i의 모든 배수를 지우기
            for j in range(2*i,n+1,i):
                a[j] = False
    
    # m 전까지 모두 False로 바꿈
    for k in range(m):
        a[k] = False
        
    return [ i for i in range(2, n+1) if a[i] ]

m,n = map(int,input().split())
x = isPrime(m,n)

print('\n'.join(map(str,x)))
```



---



**처음 작성한 코드**

```python
m,n = map(int,input().split())
for num in range(m,n+1):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    if flag:
        print(num)
```



### References

- [소수 구하기 - 에라토스테네스의 체](https://wikidocs.net/21638)

- [내가 보려고 적는 파이썬 - 소수 판별(에라토스테네스의 체)](https://velog.io/@koyo/python-is-prime-number)

- [리스트 차집합 한줄로 구현하기](https://velog.io/@koyo/python-is-prime-number)