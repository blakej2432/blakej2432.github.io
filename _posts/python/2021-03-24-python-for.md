---
title: "[python 문법] for문 정리"
date: 2021-03-24 18:58:28 +0900
categories: python
tags: python
header:
  teaser: "../../img/cover/python.png"
---

## 1. for in 반복문

- 여타 다른 언어에서는 일반적인 `for`문, `foreach`문, `for of`문등 여러가지 방식을 한꺼번에 지원하는 경우가 많지만, Python에서는 `for in`문 한가지 방식의 for 문만 제공합니다.

```python
 for i in var_list:
     print(i)
```



## 2. range

- range는 `range(시작숫자, 종료숫자, step)`의 형태로 리스트 슬라이싱과 유사합니다.

- 파이썬에서<span style="color:red"> 권장하지 않는 </span>패턴

  ```python
   s = [1, 3, 5]
   for i in range(len(s)):
       print(s[i])
          
  # 1
  # 3
  # 5
  ```

- 파이썬에서<span style="color:blue"> 권장하는 </span>패턴

  ```python
   for v in s:
       print(v)
      
  # 1
  # 3
  # 5
  ```



## 3. enumerate

- 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
- 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.

```python
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
     print(p)
        
# (0, 1)
# (1, 5)
# (2, 7)
# (3, 33)
# (4, 39)
# (5, 52)
```





### References

[파이썬 기본을 갈고 닦자 - 19. for in 반복문, Range, enumerate](https://wikidocs.net/16045)