---
title: "[프로그래머스] 메뉴 리뉴얼"
date: 2021-03-26 18:58:28 +0900
tags: python
categories: programmers
header:
  teaser: "../../img/cover/programmers.png"
---


> 2021 KAKAO BLIND RECRUITMENT 문제입니다.

```python
from itertools import combinations
import collections

def solution(orders, course):
    answer = []
    for i in course:
        course_arr = []
        for order in orders:
            if len(order)<i:
                continue
            # 'ABC' -> ['A','B','C'] -> [['A','B'],['A','C'],['B','C']]
            course_arr += combinations(sorted(order),i)

        if course_arr:
            count = collections.Counter(course_arr)
            max_value = max(list(count.values()))
            
            # 최소 2명이상의 손님으로부터 주문
            if max_value<2:
                continue
            for key in list(count.keys()):
                if count[key] == max_value:
                    answer.append(''.join(key))
    
    return sorted(answer)
```

