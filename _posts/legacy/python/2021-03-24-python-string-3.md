---
title: "[python] 파이썬 string 활용-3"
date: 2021-03-24 18:58:28 +0900
tags: python
categories: python
header:
  teaser: "../../img/cover/python.png"
---



### BOJ 1316 - 그룹 단어 체커

```python
n = int(input())
count = 0

def checker(x):
    v = [0]*123
    for i in range(len(x)):
        if v[ord(x[i])]==0:
            v[ord(x[i])]=1
        else:
            if x[i-1]!=x[i]:
                return False
            
    return True
    
for _ in range(n):
    x = list(input())
    if checker(x):
        count += 1
    
print(count)
```

###### 다른 사람의 풀이 - 숏코딩

s.find 부분이 이해가 잘 가지 않는다...아직 문법이 익숙하지가 않아서 그런 것 같다.
아마 그냥 `sorted(s)`를 하면 happy가 [a,h,p,p,y] 가 될 텐데 우리가 원하는 것은 [h,a,p,p,y]로 기존 알파벳을 기준으로 정렬하는 것이기 때문일 것 같다.

```python
a = 0
for i in range(int(input())):
    s = input()
    a+=list(s) == sorted(s, key=s.find)
print(a)
```



### [파이썬] 정렬함수 sort()와 sorted()

`sorted()`라는 정렬함수는 시퀀스 자료형 뿐만 아니라 순서에 구애받지 않는 자료형에도 적용할 수 있다.
기존의 리스트를 변경하는 것이아니고, 정렬된 결과를 list로 반환한다.

```python
#str
sorted("hello") # ["e","h","l","l","o"]

#list
sorted([5,2,1,3,4]) # ["1","2","3","4","5"]
sorted([[2,1,3],[3,2,1],[1,2,3]]) # [[1, 2, 3], [2, 1, 3], [3, 2, 1]]

#set
sorted({3,2,1}) # [1,2,3]

#tuple
sorted((3,2,1)) # [1,2,3]

#dict
sorted({3:1,2:3,1:4}) # [1,2,3]
```

`sort()`라는 리스트 메소드는 리스트 자체를 정렬된 상태로 변경하기 때문에, 일반저그올 `sorted()`가 조금 더 편리하다.

```python
myList = [4,2,3,5,1]
myList.sort()
myList #[1,2,3,4,5]
```



#### key 매개변수

객체의 데이터 중에서 특정한 데이터를 기준으로 정렬하기 위해 **key 매개변수**로 정렬을 하기전에 각 요소에 대하여 적용되는 함수를 지정할 수 있다.

```python
# 2번째 문자를 기준으로 정렬(각각 e, y, i)
myList =  ["hello", "python" , "hi"]
sorted(myList, key=lambda x:x[1]) # ["hello", "hi", "python"]
```



#### 내림차순 정렬

파라미터 `reverse` 값을 `True`로 만들어준다.

```python
sorted(range(1,10),reverse=True)
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
```



### [파이썬] array[::] 용법

`arr[::]`, `arr[1:2:3]`, `arr[::-1]` 등으로 배열의 index에 접근하는 방법을 **Extended Slices** 라고 부른다.
`arr[A:B:C]` 는 <mark>index A 부터 index B까지 C의 간격으로 배열을 만들어라</mark>라는 말이다.

```python
arr = range(10)
# [0,1,2,3,4,5,6,7,8,9]
```

```python
arr[::-1]
# 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
# [9,8,7,6,5,4,3,2,1,0]

>> arr[1::2]
# index 1 부터 끝까지 두 칸 간격으로
# [1,3,5,7,9]
```



### References

- [[python-기초] 파이썬 정렬함수(sorted)](https://bit.ly/3shkkPr)
- [[Python] sort()와 sorted()로 정렬하기](https://cigiko.cafe24.com/python-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-sort%EC%99%80-sorted/)

- [Wonkyung's blog - [Tip\] Python Array[::] 사용법](https://blog.wonkyunglee.io/3)