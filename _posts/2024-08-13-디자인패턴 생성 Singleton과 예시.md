---
layout: post
title: ""
date: 2024-08-13 23:07 +0900
categories:
  - 디자인패턴
  - Singleton
tags: 
math: true
---

## 싱글톤(Singleton) 디자인패턴

### Singleton이란?

클래스가 하나의 인스턴스만 가질 수 있도록 하는 생성 패턴

두 가지 문제를 한번에 해결
1. 클래스가 단 하나의 인스턴스를 갖는다
2. 그 인스턴스에 대한 전역적 접근 지점을 제공한다

- 데이터베이스나 특정 파일처럼 공유되는 리소스에 대해 사용자가 같은 결과를 함께 제어하는 경우
- 전역 변수처럼 어디에서든 참조할 수 있지만, 그 안의 내용은 덮어씌워지기 바라지 않는 경우


### Singleton의 구현 방식

해당 클래스의 인스턴스가 존재하지 않으면, 클래스 선언시 인스턴스를 생성하고
해당 클래스의 인스턴스가 존재하면 그 존재하는 인스턴스를 반환하는 방식

다음의 방법으로 구체화 할 수 있다.
<strong> 메타클래스 활용 / 베이스 클래스 활용 / 데코레이터 활용 </strong>


### 사용 예시

"프린터" 기기 사용시, 여러 사용자가 인쇄 문서의 대기열을 공유하고, 출력 기능을 수행해야 한다.

```python
# 프린터 기능 싱글톤 구현

# 메타클래스 활용

class Singleton(type):
    _instance = {}

  
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]
        

class Printer(metaclass=Singleton):
    def __init__(self) -> None:
        self._ready_docs = []

    def print_document(self, doc):
        self._ready_docs.append(doc)
        print(f"{doc} 문서의 인쇄가 대기열로 들어갑니다.")

    def get_ready_docs(self):
        print(self._ready_docs)


# 데코레이터 활용

def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
  

@singleton
class Printer():
    def __init__(self) -> None:
        self._ready_docs = []


    def print_document(self, doc):
        self._ready_docs.append(doc)
        
        print(f"{doc} 문서의 인쇄가 대기열로 들어갑니다.")
        
    def get_ready_docs(self):
        print(self._ready_docs)
  

p = Printer()

doc1 = "1번 문서"

p.print_document(doc1)
p.get_ready_docs()

# ['1번 문서']


j = Printer()

doc2 = "2번 문서"

j.print_document(doc2)
j.get_ready_docs()

# ['1번 문서', '2번 문서']
```


p, j 서로 다른 인스턴스를 선언한 듯 보이지만, 하나의 대기열을 공유하는 것을 볼 수 있음

