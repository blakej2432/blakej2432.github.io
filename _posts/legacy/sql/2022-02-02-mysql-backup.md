---
title: "[mysql] mysql에서 백업하기"
date: 2022-02-02 16:40:28 +0900
categories: sql
tags: 
  - mysql
  - backup
---



내가 백업할 사항은 다음과 같다.

- 테이블
- VIEW
- 데이터
- 프로시저



사실 나는 데이터 백업에 대해 두려움이 있다. 전에 AWS RDS를 사용했었는데, CLOB 형 자료가 제대로 백업되지 않는 문제가 있었는데..어정쩡 넘어갔다. 그리고 한번에 백업하려고 하면 자꾸 어디선가 오류가 나서 한땀한땀 백업을 한다🥲

찾아보았더니 mysql은 보통 dump라는 걸 사용해서 백업을 하더라. 



### 데이터 백업 명령어

```sql
mysqldump --routines –trigger –uroot -ppassword databasename > dump.sql
```



### Procedure, Function, Trigger, Event 포함 백업 명령어

```sql
mysqldump --routines –trigger –uroot -ppassword databasename > dump.sql
```



<br/>

근데 나는 Azure에 있는 mysql에 접속해서 백업을 해야하는데, 그러면 리눅스로 된 Azure VM을 또 만들어서 mysql을 설치하고 접속하고..해야해서, 포기하고 한땀한땀 백업했다. 어차피 데이터가 많은 것도 아니라서.

그래서 결국 해본 건 아니지만, 내 pc에서 작업하게 되면 해당명령어로 편하게 백업하면 되겠다ㅎㅎ



<br/>

**REFERENCES**

- [MySQL Dump시 Procedure, Function, Trigger 포함하여 백업하기](https://storytown.tistory.com/19)