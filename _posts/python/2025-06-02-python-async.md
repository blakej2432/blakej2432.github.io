---
title: "[Python] 파이썬 비동기와 코루틴 (feat. I/O, cpu 바운드)"
date: 2025-06-01 18:24:28 +0900
categories: python
tags: python async await 비동기
header:
  teaser: "../../img/cover/python_logo.svg"
---

비동기를 이해하려면 바운드 상황을 먼저 이해해야 한다.

특정 조건 때문에 성능이 제한되는(완료하는데 시간이 소요되는) 상황이 **바운드(bound)** 이다.
바운드가 생길 때, 코드 실행이 멈춰 있는 현상이 **블로킹(blocking)** 이다.

### I/O 바운드란?
- 네트워크에서 데이터를 요청하거나 받는 것
- 디스크에 파일을 저장하거나 읽는 것
- DB에 쿼리를 던지고 결과를 받는 것
- 사용자에게 입력을 기다리는 것

으로 인해 발생하면 I/O 바운드이다. 여기서의 I/O는 단순히 사용자 입력과 프로그램의 반환값이 아니라 CPU와 CPU 외부의 모든 데이터 교환을 의미한다.

예컨대, 특정 네트워크에 request해서 응답을 기다리는 경우, cpu가 대기하고 있을 때도 해당한다.

=> **I/O 응답 시간이 프로그램 실행 속도 결정**

------

### cpu 바운드란?
- 너무 복잡한 연산이나, 많은량의 작업을 처리하는 경우
에 연산을 하느라고 다음 진행이 안되는 경우 cpu 바운드가 발생한다.

=> **CPU 실행 속도가 프로그램 실행 속도 결정**

ex)
```python
for i in range(1, 1000):
    for j in range(1, 1000):
        for z in range(1, 1000):
            print(i * j * z)
```

------

### 동기와 비동기
- **동기**(Sync)는 코드가 작성 순서대로 실행되는 것
- **비동기**(Async)는 코드가 특정 작업의 완료를 기다리지 않고도 실행될 수 있는 것


위에서 말한 **I/O 바운드 상황**에 비동기로 구현하여 효율성을 높일 수 있다.

```python
# 비동기로 메일 전달, 답장 전달 구현 예시
import time
import asyncio


async def send_email(name, response_time):
    print(f"{name}에게 메일전달")
    await asyncio.sleep(response_time)
    print(f"{name} 답장 완료, {response_time}시간 소요...")
    return response_time


async def main():
    result = await asyncio.gather(
        send_email("A", 1),
        send_email("B", 2),
        send_email("C", 3),
    )
    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
```

> A에게 메일전달<br>
> B에게 메일전달<br>
> C에게 메일전달<br>
> A 답장 완료, 1시간 소요...<br>
> B 답장 완료, 2시간 소요...<br>
> C 답장 완료, 3시간 소요...<br>
> [1, 2, 3]<br>
> 3.0021135807037354<br>


1. 한 사람에게 메일을 보내고, 답장을 받기전에 다음 사람에게 메일을 보낸다.

2. await 하고 있던 작업(답장)이 실행된다.


동기적으로 구현했다면, 6초 이상 걸림 -> 약 3초로 해결


### 코루틴 이란?

루틴은 코드의 흐름이다. 
- 메인 루틴: 프로그램의 메인 코드의 흐름으로, 여기서는 main 함수
- 서브 루틴: 메인 루틴을 보조하는 보통의 함수나 메서드(하나의 진입점, 하나의 탈출점)
- **코루틴**: 다양한 진입점과 탈출점이 있는 함수, 비동기로 구현한 아래 예시 함수가 코루틴이다.

```python
async def send_email(name, response_time):
    print(f"{name}에게 메일전달")
    await asyncio.sleep(response_time)
    print(f"{name} 답장 완료, {response_time}시간 소요...")
    return response_time
```

이 함수는 첫줄에서 진입(1)하고, await를 만나 탈출(1), 다시 await의 asyncio.sleep에서 진입(2), return에서 탈출(2)

