---
title: "[python] 파이썬 string 활용-1"
date: 2021-03-22 18:58:28 +0900
categories: python
tags: python
header:
  teaser: "../../img/cover/python.png"
---

### 오늘의 한마디

오늘 삼성 자소서에 썼던 이동진의 '그럼에도 불구하고...' 나는 이 말이 참 좋다.

> 기본적으로 평론은 ‘그럼에도 불구하고’의 세계라고 생각해요. 앞의 전제에 대해 인정하거나 인지한다는 걸 전제하잖아요. 그게 작품과 평론가의 관계 아닐까요? 어떤 평론은 작품 자체를 완전히 깔아뭉개고 시작하는 경우도 있지만, 기본적으로는 바람직하지 않다고 생각해요. 일단 그 영화가 한 말은 들은 다음, ‘그럼에도 불구하고’ 제 말을 쓰는 거죠. 사람이 다 자기 사연이 있고 할 말이 있어요. 아무리 이상한 사람도 그렇게 행동할 최소한의 이유가 있는 거예요. 그럼에도 불구하고 모든 일에 ‘너도 옳고 나도 옳으니까 여기서 끝내자’라고는 할 수 없어요. 그러니 상대방을 인정하고 들어준다는 전제 아래 제가 하고 싶은 말을 조심스럽게 하는 거죠.
>
> ━ 이동진 평론가



<br>

### [파이썬] 리스트 순서 거꾸로 뒤집기

###### reverse()

: 아무값도 반환하지 않으면서, 리스트에 있는 값의 순서를 거꾸로 뒤집는다.

```python
list = [0,10,20,40]
list.reverse()
print(list)

# [40, 20, 10, 0]
```



### BOJ 2908 - 상수

```python
a, b = input().split(' ')
arr_a = list(a)
arr_b = list(b)
arr_a.reverse()
arr_b.reverse()
rev_a = int(''.join(arr_a))
rev_b = int(''.join(arr_b))

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)
```

### BOJ 5622 - 다이얼

```python
x = list(input())
v = []

# 알파벳에 해당하는 숫자 구하기
def getNum(a):
    code = ord(a)
    num = 0
    if code==90:
        num = 9
    elif code==83:
        num = 7
    else:
        if code<83:
            num = (code-59)//3
        else:
            num = (code-60)//3
    return num
        
for i in range(len(x)):
    v.append(getNum(x[i]))
    
# 숫자에 해당하는 시간구하기    
print(sum(v)+len(v))
```



<br>

### References

[[Python] 리스트(배열) 순서 거꾸로 뒤집기]([Python] 리스트(배열) 순서 거꾸로 뒤집기)

[이동진 - 평론은 ''그럼에도 불구하고''의 세계](http://ch.yes24.com/Article/View/40114)