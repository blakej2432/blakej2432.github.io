---
title: "[프로그래머스] 광고 삽입"
date: 2021-03-26 18:58:28 +0900
categories: programmers
tags: python
header:
  teaser: "../../img/cover/programmers.png"
---

> 2021 KAKAO BLIND RECRUITMENT 문제입니다.

### 처음 풀었던 풀이
첫번째 테스트게이스를 제외하고 시간초과에 걸려서 통과하지 못했다.
for문 안에서 sum 함수를 쓴 원인과, 이중for문, time 라이브러리를 사용한 것이 주요한 문제였다.
(for문 안에서 일일히 sum으로 값을 구한게 너무 비효율적이긴 했다..)

```python
import time

#HH:MM:SS문자열을 시간(초)로 변환
def convert_to_sec(a):
    t = list(map(int,a.split(':')))
    return t[0]*3600 + t[1]*60 + t[2]

def solution(play_time, adv_time, logs):
    # 초로 변환
    play_time_sec = convert_to_sec(play_time)
    adv_time_sec = convert_to_sec(adv_time)
    
    # 전체 시간을 초단위로 저장하는 배열
    x = [0] * (play_time_sec + 1)
    for i in logs:
        prev, post = i.split('-')
        prev_sec = convert_to_sec(prev)
        post_sec = convert_to_sec(post)
        for j in range(prev_sec,post_sec+1):
            x[j] +=1

    #시간을 곱해서 생기는 누적 재생시간의 max값을 구한다
    acc_max = 0
    max_time = 0
    for i in range(len(x)):
        acc = sum(x[i+1:i+adv_time_sec+1])
        # 이전 값보다 클 경우 갱신
        # 이전 값과 작거나 같을 경우 갱신하지 않음
        if acc_max < acc:
            print(acc)
            acc_max = acc
            max_time = i
    
    answer = time.strftime('%H:%M:%S', time.gmtime(max_time))
    return answer
```



### 최종 풀이

```python
# HH:MM:SS문자열을 시간(초)로 변환
def convert_to_sec(a):
    t = list(map(int,a.split(':')))
    return t[0]*3600 + t[1]*60 + t[2]
# 초를 HH:MM:SS문자열로 변환
def sec_to_time(seconds):
    s = seconds % 60
    seconds//= 60
    m = seconds % 60
    seconds //= 60
    h = seconds 
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

def solution(play_time, adv_time, logs):
    # 초로 변환
    play_time_sec = convert_to_sec(play_time)
    adv_time_sec = convert_to_sec(adv_time)
    
    # 전체 시간을 초단위로 저장하는 배열
    # 시작하는 지점을 1, 끝나는 지점을 -1로 저장
    total_played = [0] * (play_time_sec + 1)
    for i in logs:
        prev, post = i.split('-')
        prev_sec = convert_to_sec(prev)
        post_sec = convert_to_sec(post)
        total_played[prev_sec] += 1
        total_played[post_sec] -= 1

    # 각 구간별 재생횟수 구하기
    for idx in range(1, play_time_sec+1):
        total_played[idx] += total_played[idx-1]
    # 재생횟수의 총합 == 누적 재생시간(초)
    for idx in range(1, play_time_sec+1):
        total_played[idx] += total_played[idx-1]

    # 00초부터 시작했을 때의 최댓값을 기본으로 잡는다.
    max_time = 0
    max_sum_played = total_played[adv_time_sec]
    for start_time in range(1, play_time_sec):
        if start_time + adv_time_sec < play_time_sec:
            end_time = start_time + adv_time_sec
        else:
            end_time = play_time_sec
        sum_played = total_played[end_time] - total_played[start_time]
        if max_sum_played < sum_played:
            max_sum_played = sum_played
            max_time = start_time+1

    answer = sec_to_time(max_time)
    return answer
```

### References

- 문제
  - [프로그래머스 - 광고 삽입](https://programmers.co.kr/learn/courses/30/lessons/72414)
- 해설참조
  - [[Python] 프로그래머스. 2021 카카오 recruit - 광고 삽입 (Level 3)](https://inspirit941.tistory.com/348)

